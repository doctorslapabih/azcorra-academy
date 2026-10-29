// IQ Lab registry.
import * as matrix from "./matrix.js";
import * as series from "./series.js";
import * as span from "./span.js";
import * as nback from "./nback.js";
import * as speed from "./speed.js";
import * as rotation from "./rotation.js";
import * as analogies from "./analogies.js";
import * as logic from "./logic.js";

export const GAMES = [matrix, series, logic, analogies, span, nback, speed, rotation];

export const ABILITIES = [
  { id: "gf", name: "Fluid reasoning", desc: "Solving new problems you've never seen" },
  { id: "gq", name: "Quantitative reasoning", desc: "Reasoning with numbers and patterns" },
  { id: "logic", name: "Logical reasoning", desc: "Deduction and catching traps" },
  { id: "gc", name: "Verbal knowledge", desc: "Words and how ideas relate" },
  { id: "gwm", name: "Working memory", desc: "Holding and juggling info in your head" },
  { id: "gs", name: "Processing speed", desc: "Doing simple tasks fast and accurately" },
  { id: "gv", name: "Visual-spatial", desc: "Picturing and turning shapes" }
];

export function find(id) { return GAMES.find(g => g.meta.id === id); }
