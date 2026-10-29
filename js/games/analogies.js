// Verbal Analogies — A is to B as C is to ? Builds vocabulary and relational reasoning.
import { shuffle } from "../ui.js";
import { intro, finish, runChoiceSession, levelNorm, nextLevel } from "./common.js";
import { ANALOGIES } from "./banks.js";
import * as store from "../store.js";

const MAX = 3, TOTAL = 10;

export const meta = {
  id: "analogies", title: "Verbal Analogies", ability: "gc", abilityName: "Verbal knowledge",
  blurb: "A is to B as C is to what? Vocabulary plus the logic of relationships.", minutes: 5
};

export function mount(root) {
  intro(root, meta, `
    <p>Read <strong>HOT : COLD :: TALL : ?</strong> as "hot is to cold as tall is to what?"</p>
    <p>Method: say the relationship in a full sentence first. "Hot is the opposite of cold." Then plug the second pair into the same sentence: "Tall is the opposite of…" If two options fit, make your sentence more specific.</p>
    <p>Common relationships: opposites, part to whole, worker to tool, young to adult, group names, cause to effect, and degree (warm to scorching).</p>
    <p>Ten items, currently <strong>level ${store.level("analogies")} of ${MAX}</strong>.</p>`, () => play(root));
}

function play(root) {
  const level = store.level("analogies");
  const main = shuffle(ANALOGIES.filter(a => a.lvl === level));
  const extra = shuffle(ANALOGIES.filter(a => a.lvl !== level && Math.abs(a.lvl - level) === 1));
  const items = main.slice(0, 7).concat(extra).slice(0, TOTAL).map(x => Object.assign({}, x, { _order: null }));
  runChoiceSession(root, meta, shuffle(items), {
    onDone: (score, review) => {
      const acc = Math.round((score / items.length) * 100);
      const nl = nextLevel(level, acc, MAX);
      store.level("analogies", nl);
      finish(root, meta, { score, max: items.length, level, newLevel: nl, norm: levelNorm(level, MAX, acc), metric: `level ${level}`, summary: "Every miss here is a word or relationship to add to your notebook.", review }, () => play(root));
    }
  });
}
