// Logic & Riddles — classic reasoning traps, syllogisms and puzzles with full explanations.
import { shuffle } from "../ui.js";
import { intro, finish, runChoiceSession, clamp } from "./common.js";
import { LOGIC } from "./banks.js";

const TOTAL = 10;

export const meta = {
  id: "logic", title: "Logic & Riddles", ability: "logic", abilityName: "Logical reasoning",
  blurb: "Traps your gut falls for, syllogisms, and classic puzzles.", minutes: 6
};

export function mount(root) {
  intro(root, meta, `
    <p>These are built to make your first instinct wrong. The skill being trained is <strong>catching yourself</strong>: pausing, then checking the gut answer before you lock it in.</p>
    <p>Method: restate the question in your own words, write the numbers down, and test your answer against every condition in the question.</p>`, () => play(root));
}

function play(root) {
  const items = shuffle(LOGIC).slice(0, TOTAL).map(x => Object.assign({}, x, { _order: null }));
  runChoiceSession(root, meta, items, {
    onDone: (score, review) => {
      const acc = Math.round((score / items.length) * 100);
      finish(root, meta, { score, max: items.length, level: 0, newLevel: 0, norm: Math.round(clamp(acc)), metric: "", summary: "Read every explanation, even on the ones you got right. The method is the point.", review }, () => play(root));
    }
  });
}
