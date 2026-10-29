from common import *
L = []
L.append({"id": "atoms-and-their-parts", "title": "Atoms and their parts", "band": "Grades 7–8", "minutes": 16,
 "lede": "Everything you can touch is made of atoms. Here's what's inside one.",
 "sections": [
  T("## The three particles\n| Particle | Charge | Where | Mass |\n|---|---|---|---|\n| Proton | + | nucleus | about 1 unit |\n| Neutron | none | nucleus | about 1 unit |\n| Electron | − | around the nucleus | about 1/1,836 of a proton |\n\nThe nucleus is tiny but holds almost all the mass. Electrons move in the space around it, and that space is most of the atom."),
  T("## What makes an element\nThe number of **protons** decides the element. Every carbon atom has 6 protons; every oxygen atom has 8. That number is the **atomic number**.\n\n- Change the neutrons and you get an **isotope** of the same element (carbon-12 vs carbon-14).\n- Change the electrons and you get an **ion**, an atom with a charge."),
  E("Count the particles", "Sodium (Na) has atomic number 11 and mass number 23. How many protons, neutrons and electrons in a neutral atom?",
    ["Protons = atomic number = 11.", "Neutrons = mass number − protons = 23 − 11 = 12.", "Neutral means electrons = protons = 11."], "**11 protons, 12 neutrons, 11 electrons**"),
  N("Why atoms bond", "Chemistry is mostly about electrons, especially the outermost ones. Atoms gain, lose or share electrons to reach a stable arrangement. That's what holds molecules together.")
 ],
 "practice": [
  MC("Which particle has no charge?", ["Proton", "Neutron", "Electron", "Ion"], 1, "Neutral = neutron."),
  MC("What decides which element an atom is?", ["Number of neutrons", "Number of electrons", "Number of protons", "Its size"], 2, "Atomic number = protons."),
  NUM("Carbon has atomic number 6. A carbon-14 atom has how many neutrons?", 8, "14 − 6."),
  MC("Where is almost all of an atom's mass?", ["Electron cloud", "Nucleus", "Spread evenly", "Outside the atom"], 1, "Protons and neutrons are in the nucleus."),
  MC("An atom that gains an electron becomes…", ["A positive ion", "A negative ion", "An isotope", "A new element"], 1, "Extra negative charge.")
 ]})

L.append({"id": "the-periodic-table", "title": "The periodic table", "band": "Grades 7–8", "minutes": 16,
 "lede": "The periodic table is a map. Once you can read it, you can predict how elements behave.",
 "sections": [
  T("## How it's arranged\nElements are ordered by **atomic number** (protons), left to right, top to bottom.\n\n- **Rows (periods):** each row adds a new layer (shell) of electrons.\n- **Columns (groups):** elements in a column have the same number of outer electrons, so they behave alike."),
  T("## Neighborhoods\n| Region | Examples | Behavior |\n|---|---|---|\n| Group 1: alkali metals | sodium, potassium | very reactive, 1 outer electron |\n| Group 17: halogens | chlorine, fluorine | very reactive, want 1 more electron |\n| Group 18: noble gases | helium, neon | stable, barely react |\n| Metals (left and middle) | iron, copper | shiny, conduct electricity |\n| Nonmetals (upper right) | oxygen, carbon | poor conductors |"),
  E("Predict a reaction", "Sodium (group 1) and chlorine (group 17) meet. What happens?",
    ["Sodium has 1 outer electron it easily gives up.", "Chlorine needs 1 more electron.", "Sodium hands its electron to chlorine."], "They form **sodium chloride**: table salt."),
  N("Mendeleev's bet", "Dmitri Mendeleev arranged his 1869 table by patterns and left gaps for elements nobody had found yet. He predicted their properties, and when gallium and germanium were discovered, they matched. A good model makes predictions.")
 ],
 "practice": [
  MC("Elements in the same column have the same…", ["Mass", "Number of outer electrons", "Number of neutrons", "Color"], 1, "That's why they behave alike."),
  MC("Which group barely reacts with anything?", ["Alkali metals", "Halogens", "Noble gases", "Transition metals"], 2, "Full outer shells."),
  MC("The table is ordered by…", ["Mass", "Atomic number", "Discovery date", "Alphabet"], 1, "Number of protons."),
  MC("Sodium + chlorine forms…", ["Water", "Table salt", "Rust", "Sugar"], 1, "NaCl."),
  MC("Which is a metal?", ["Oxygen", "Neon", "Copper", "Chlorine"], 2, "Copper conducts electricity.")
 ]})

L.append({"id": "states-of-matter", "title": "States of matter", "band": "Grades 7–8", "minutes": 14,
 "lede": "Solid, liquid, gas: what's really different is how fast the particles move.",
 "sections": [
  T("## Particles in motion\nAll matter is made of particles that are always moving. Temperature is a measure of their average motion energy.\n\n| State | Particles | Shape | Volume |\n|---|---|---|---|\n| Solid | vibrate in place, tightly packed | fixed | fixed |\n| Liquid | slide past each other, close together | takes container's | fixed |\n| Gas | fly freely, far apart | fills container | fills container |"),
  T("## Changes of state\n- Melting: solid → liquid. Freezing: liquid → solid.\n- Evaporation/boiling: liquid → gas. Condensation: gas → liquid.\n- Sublimation: solid → gas directly (dry ice).\n\nDuring a change of state, temperature stays flat. The energy goes into breaking particles apart, not into speeding them up. That's why ice water stays near 0°C until the ice is gone."),
  E("Pressure and boiling", "Why does a pressure cooker cook faster?",
    ["Higher pressure makes it harder for water molecules to escape as gas.", "So water must get hotter before it boils, above 100°C.", "Hotter water cooks food faster."], "Higher pressure → **higher boiling point** → hotter cooking water."),
  N("Air brakes", "Truck air brakes run on compressed gas. Gas compresses easily because its particles are far apart. Liquids barely compress, which is why hydraulic brakes use fluid to transmit force.")
 ],
 "practice": [
  MC("In which state are particles farthest apart?", ["Solid", "Liquid", "Gas", "All equal"], 2, "Gas particles fly freely."),
  MC("Water vapor forming droplets on a cold glass is…", ["Evaporation", "Condensation", "Melting", "Sublimation"], 1, "Gas → liquid."),
  MC("While ice melts, its temperature…", ["Rises fast", "Stays about the same", "Drops", "Doubles"], 1, "Energy goes into the change of state."),
  MC("Dry ice turning straight into gas is…", ["Sublimation", "Condensation", "Freezing", "Boiling"], 0, "Solid → gas."),
  MC("Which state has a fixed volume but no fixed shape?", ["Solid", "Liquid", "Gas", "None"], 1, "Liquids take the container's shape.")
 ]})

L.append({"id": "chemical-reactions", "title": "Chemical reactions", "band": "Grade 8", "minutes": 18,
 "lede": "Atoms rearrange, nothing is lost, and equations have to balance.",
 "sections": [
  T("## Physical vs chemical change\n- **Physical change:** same substance, new form. Melting ice, crushing a can.\n- **Chemical change:** new substances form. Burning fuel, rusting steel, baking bread.\n\nSigns of a chemical change: gas bubbles, color change, heat or light given off, a new solid forming."),
  T("## Conservation of mass\nIn a reaction, atoms are rearranged, never created or destroyed. The total mass before equals the total mass after. That's why chemical equations must **balance**: the same number of each atom on both sides."),
  E("Balance an equation", "H₂ + O₂ → H₂O (hydrogen burns to make water)",
    ["Count: left has 2 O, right has 1 O.", "Put a 2 in front of H₂O: H₂ + O₂ → 2H₂O. Now O is 2 and 2, but H is 2 vs 4.", "Put a 2 in front of H₂: 2H₂ + O₂ → 2H₂O.", "Check: H 4 and 4; O 2 and 2. ✓"], "**2H₂ + O₂ → 2H₂O**"),
  T("## Energy in reactions\n- **Exothermic** reactions release energy as heat or light: burning diesel, which is how an engine turns fuel into motion.\n- **Endothermic** reactions absorb heat: an instant cold pack."),
  N("Combustion", "Burning a hydrocarbon fuel with oxygen produces carbon dioxide, water and energy. Diesel exhaust also contains other byproducts, which is why modern trucks have filters and DEF systems to clean it.")
 ],
 "practice": [
  MC("Which is a chemical change?", ["Ice melting", "Paper burning", "Glass breaking", "Sugar dissolving"], 1, "New substances form."),
  MC("In a reaction, total mass…", ["Increases", "Decreases", "Stays the same", "Disappears"], 2, "Conservation of mass."),
  MC("Balanced form of H₂ + O₂ → H₂O:", ["H₂ + O₂ → 2H₂O", "2H₂ + O₂ → 2H₂O", "H₂ + 2O₂ → H₂O", "2H₂ + 2O₂ → 2H₂O"], 1, "4 H and 2 O on each side."),
  MC("A reaction that releases heat is…", ["Endothermic", "Exothermic", "Physical", "Balanced"], 1, "Exo = out."),
  MC("Which is NOT a sign of a chemical change?", ["Gas bubbles", "Color change", "Changing shape", "Light given off"], 2, "Shape change is physical.")
 ]})
save("science", L)
