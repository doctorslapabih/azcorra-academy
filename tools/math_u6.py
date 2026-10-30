from common import *

GEO = {"title": "OpenStax, Contemporary Mathematics (Geometry chapter)", "url": "https://openstax.org/details/books/contemporary-mathematics"}
AT = {"title": "OpenStax, Algebra and Trigonometry 2e", "url": "https://openstax.org/details/books/algebra-and-trigonometry-2e"}
L = []


def FIG(svg, caption): return {"type": "figure", "svg": svg, "caption": caption}


TRI = """<svg viewBox="0 0 480 220" width="100%" style="max-width:540px" role="img" aria-label="Right triangle with sides labeled relative to angle theta">
<g font-family="inherit" font-size="14" fill="currentColor">
<path d="M40 190 L340 190 L340 40 Z" fill="currentColor" fill-opacity=".08" stroke="currentColor" stroke-width="2"/>
<path d="M322 190 L322 172 L340 172" fill="none" stroke="currentColor"/>
<path d="M95 190 A55 55 0 0 0 89 166" fill="none" stroke="currentColor"/>
<text x="102" y="180">θ</text>
<text x="160" y="210">adjacent (next to θ)</text>
<text x="348" y="118">opposite</text>
<text x="348" y="134" fill-opacity=".7">(across from θ)</text>
<text x="105" y="100" transform="rotate(-26 160 105)">hypotenuse (longest, across from 90°)</text>
</g></svg>"""

CIRC = """<svg viewBox="0 0 420 240" width="100%" style="max-width:460px" role="img" aria-label="Central angle and inscribed angle on the same arc">
<g font-family="inherit" font-size="13" fill="currentColor">
<circle cx="150" cy="120" r="100" fill="currentColor" fill-opacity=".05" stroke="currentColor" stroke-width="2"/>
<circle cx="150" cy="120" r="3"/>
<text x="138" y="112">O</text>
<line x1="150" y1="120" x2="227" y2="184" stroke="currentColor" stroke-width="2"/>
<line x1="150" y1="120" x2="227" y2="56" stroke="currentColor" stroke-width="2"/>
<line x1="52" y1="138" x2="227" y2="184" stroke="currentColor" stroke-dasharray="5 4"/>
<line x1="52" y1="138" x2="227" y2="56" stroke="currentColor" stroke-dasharray="5 4"/>
<text x="231" y="50">A</text><text x="231" y="200">B</text><text x="36" y="144">P</text>
<path d="M227 56 A100 100 0 0 1 227 184" fill="none" stroke="currentColor" stroke-width="5" stroke-opacity=".5"/>
<text x="268" y="105">central ∠AOB = 80°</text>
<text x="268" y="125">inscribed ∠APB = 40°</text>
<text x="268" y="145">arc AB = 80°</text>
</g></svg>"""

# ---------------------------------------------------------------- Logic and proof
L.append({"id": "logic-and-proof", "title": "Logic and proof", "band": "Grade 10", "minutes": 34,
 "lede": "Geometry is where math stops asking you to compute and starts asking you to prove. Learn how if-then statements work, why a single counterexample beats a thousand examples, and how to build an airtight argument.",
 "sections": [
  T("## Conditional statements\nA **conditional** is an *if–then* statement: **If p, then q.**\n\n- **p** is the **hypothesis** (the condition).\n- **q** is the **conclusion** (what follows).\n\n*If a shape is a square, then it has four right angles.*\n\nA conditional is **false** only in one situation: **p is true and q is false**. One such case, a **counterexample**, is enough to sink it."),
  T("## Four related statements\nStart with: **If it's raining, then the road is wet.** (True.)\n\n| Name | Form | Example | True? |\n|---|---|---|---|\n| **Conditional** | if p, then q | If it's raining, the road is wet. | ✓ |\n| **Converse** | if q, then p | If the road is wet, it's raining. | ✗ (sprinklers, a spill) |\n| **Inverse** | if not p, then not q | If it's not raining, the road isn't wet. | ✗ |\n| **Contrapositive** | if not q, then not p | If the road isn't wet, it isn't raining. | ✓ |\n\n**The key fact:** a statement and its **contrapositive** are always **both true or both false**. The converse and inverse can go either way.\n\nWhen both a statement and its converse are true, combine them into a **biconditional** with *if and only if*: *An angle is right **if and only if** it measures 90°.* That's what a good definition is."),
  CHECK("\"If you passed the CDL test, then you studied.\" The **contrapositive** is…", ["If you studied, you passed.", "If you didn't pass, you didn't study.", "If you didn't study, you didn't pass.", "You passed and studied."], 2, "Flip **and** negate both parts: if not q, then not p."),
  T("## Two kinds of reasoning\n- **Inductive reasoning** spots a **pattern** in examples and guesses a rule. *The last 5 Mondays the market opened weak, so Mondays open weak.* Useful for making guesses, called **conjectures**, but never proof.\n- **Deductive reasoning** uses **facts, definitions and accepted rules** to reach a conclusion that **must** be true. That's a proof.\n\nThe classic deductive pattern (**law of detachment**):\n1. If an angle is a right angle, it measures 90°. *(rule)*\n2. ∠A is a right angle. *(fact)*\n3. Therefore ∠A measures 90°. *(must follow)*\n\nTrading is mostly inductive: patterns that **tend** to hold. That's exactly why you need risk management: inductive conclusions can fail."),
  E("One counterexample", "Conjecture: *For every number n, n² is greater than n.*",
    ["Try n = 3: 9 > 3 ✓. Try n = 10: 100 > 10 ✓.", "Try n = 1: 1 > 1? ✗.", "Try n = 0.5: 0.25 > 0.5? ✗."],
    "**False.** A million examples can't prove a universal claim. **One** counterexample destroys it."),
  T("## The facts proofs are built from\n| Fact | Says |\n|---|---|\n| **Vertical angles** | the opposite angles where two lines cross are **equal** |\n| **Linear pair** | two angles forming a straight line add to **180°** |\n| **Triangle sum** | a triangle's angles add to **180°** |\n| **Reflexive** | anything equals itself (AB = AB) |\n| **Substitution** | equal things can replace each other |\n| **Transitive** | if a = b and b = c, then a = c |\n| **Parallel lines cut by a transversal** | alternate interior angles are equal; corresponding angles are equal |"),
  T("## A two-column proof\n**Given:** lines intersect, forming ∠1 and ∠2 as a linear pair and ∠2 and ∠3 as a linear pair.\n**Prove:** ∠1 = ∠3 (vertical angles are equal).\n\n| Statement | Reason |\n|---|---|\n| 1. ∠1 + ∠2 = 180° | linear pair |\n| 2. ∠2 + ∠3 = 180° | linear pair |\n| 3. ∠1 + ∠2 = ∠2 + ∠3 | substitution (both equal 180°) |\n| 4. ∠1 = ∠3 | subtract ∠2 from both sides |\n\nEvery line needs a **reason** that's a definition, a given, or a previously proven fact. *It looks equal* is never a reason."),
  CHECK("Which is a valid reason in a proof?", ["It looks like a right angle.", "The diagram shows it.", "Vertical angles are equal.", "I measured it with a protractor."], 2, "Only proven facts, definitions and givens count. Diagrams can be drawn wrong."),
  N("Common traps", "- **Assuming the converse.** *All squares are rectangles* doesn't mean all rectangles are squares.\n- **Mixing up inverse and contrapositive.** Contrapositive flips **and** negates. Inverse only negates.\n- **Treating a pattern as a proof.** Inductive evidence suggests; deductive reasoning proves.\n- **Trusting the diagram.** Unless it's marked or given, it isn't known.")
 ],
 "practice": [
  MC("In \"If a number is even, then it's divisible by 2,\" the hypothesis is…", ["it's divisible by 2", "a number is even", "if", "the whole sentence"], 1, "The part after *if*."),
  MC("The **converse** of \"If x = 3, then x² = 9\" is…", ["If x² = 9, then x = 3.", "If x ≠ 3, then x² ≠ 9.", "If x² ≠ 9, then x ≠ 3.", "x = 3 and x² = 9"], 0, "Swap hypothesis and conclusion."),
  MC("Is that converse true?", ["Yes, always", "No: x could be −3", "Only for positive numbers, so yes", "Converses are always false"], 1, "(−3)² = 9 too: a counterexample."),
  MC("A statement is always logically equivalent to its…", ["converse", "inverse", "contrapositive", "negation"], 2, "Same truth value, always."),
  MC("\"Every swan I've seen is white, so all swans are white\" is…", ["deductive reasoning", "inductive reasoning", "a proof", "a contrapositive"], 1, "Pattern → guess. (Black swans exist in Australia.)"),
  NUM("Two lines cross. One angle is 65°. What is its **vertical** angle?", 65, "Vertical angles are equal.", unit="°"),
  NUM("Two lines cross. One angle is 65°. What is the angle forming a **linear pair** with it?", 115, "180 − 65 = 115.", unit="°"),
  MC("How many counterexamples do you need to disprove \"all\" statements?", ["one", "ten", "half the cases", "all of them"], 0, "One is enough."),
  MC("\"If a quadrilateral is a square, then it's a rectangle.\" Which pair is **both true**?", ["conditional and converse", "conditional and contrapositive", "converse and contrapositive", "inverse and contrapositive"], 1,
     "The conditional is true, so its contrapositive (*if not a rectangle, then not a square*) is too. The converse (*rectangle → square*) is false.",
     level="challenge", hint="Which statement always matches the original?"),
  MC("Given: \"If you follow your rules, you won't blow your account.\" You blew your account. Logically you can conclude…", ["You followed your rules.", "You didn't follow your rules.", "Nothing.", "The rules are bad."], 1,
     "This is the contrapositive at work (called *modus tollens*): not q → not p. If the original statement is true, blowing the account means the rules weren't followed.",
     level="challenge", hint="Use the contrapositive."),
  NUM("In a triangle, one angle is 90° and another is 37°. Using the triangle sum, find the third.", 53,
      "180 − 90 − 37 = **53°**.",
      level="challenge", hint="All three add to 180°.", unit="°"),
  MC("Which is a correct **biconditional** (true both ways)?", ["A number is divisible by 4 if and only if it's even.", "A triangle has a 90° angle if and only if it's a right triangle.", "A shape is a square if and only if it has four sides.", "It's raining if and only if the ground is wet."], 1,
     "That's the definition of a right triangle, so it works in both directions. The others fail one direction (6 is even, not divisible by 4; rectangles have four sides; sprinklers wet the ground).",
     level="challenge", hint="Test each in reverse."),
 ],
 "sources": [GEO, {"title": "OpenStax, Contemporary Mathematics, 2.5 Equivalent Statements", "url": "https://openstax.org/books/contemporary-mathematics/pages/2-5-equivalent-statements"}]})

# ---------------------------------------------------------------- Congruence and similarity
L.append({"id": "congruence-and-similarity", "title": "Congruence and similarity", "band": "Grade 10", "minutes": 34,
 "lede": "Same shape and size, or same shape at a different scale. The ideas behind blueprints, maps, model trucks and measuring a tree with its shadow.",
 "sections": [
  T("## Congruent: identical copies\nTwo figures are **congruent** (≅) if one can be moved onto the other by **sliding, flipping or turning**, with no stretching. All matching sides and all matching angles are equal.\n\nTo prove two **triangles** congruent, you don't need all six parts. These shortcuts are enough:\n\n| Shortcut | What must match |\n|---|---|\n| **SSS** | all three sides |\n| **SAS** | two sides and the angle **between** them |\n| **ASA** | two angles and the side **between** them |\n| **AAS** | two angles and a side **not** between them |\n| **HL** | (right triangles only) hypotenuse and one leg |\n\n**These don't work:**\n- **AAA**: same angles can come in any size (that's similarity, not congruence).\n- **SSA**: two sides and a non-included angle can make two different triangles."),
  CHECK("Two triangles have all three angles equal. Are they congruent?", ["Yes, AAA", "Not necessarily: one could be a bigger copy", "Yes, if they're right triangles", "Only if they're equilateral"], 1, "AAA only guarantees the same **shape**."),
  T("## CPCTC\nOnce you prove two triangles congruent, every other matching part is equal too: **Corresponding Parts of Congruent Triangles are Congruent.** Proofs often prove triangles congruent as a stepping stone, then use CPCTC to get the side or angle they actually wanted."),
  T("## Similar: same shape, different size\nTwo figures are **similar** (∼) when all angles match and all side lengths are in the **same ratio**, called the **scale factor** k.\n\nFor triangles, shortcuts again:\n\n| Shortcut | What must hold |\n|---|---|\n| **AA** | two angles match (the third must too) |\n| **SSS∼** | all three side ratios are equal |\n| **SAS∼** | two side ratios equal and the angle between them matches |\n\n**Set up a proportion with matching sides:** small ÷ big = small ÷ big."),
  E("The shadow trick", "You're 6 ft tall and cast a 4 ft shadow. At the same moment, a light pole casts a 20 ft shadow. How tall is the pole?",
    ["The Sun hits both at the same angle, and both stand straight up: the triangles are similar (AA).", "height ÷ shadow is the same: 6/4 = h/20.", "h = 20 × 6 ÷ 4 = 30."], "**30 ft.** Ancient Greek mathematician Thales is said to have measured the height of a pyramid this way."),
  T("## Scale factor: lengths, areas, volumes\nIf a figure is scaled by **k**:\n\n| Measure | Multiplies by |\n|---|---|\n| lengths (sides, perimeter) | **k** |\n| areas | **k²** |\n| volumes | **k³** |\n\nDouble every dimension of a box (k = 2): its surface area becomes **4×**, its volume **8×**.\n\nThis is why giant animals can't just be scaled-up small ones: weight grows with volume (k³) while bone strength grows with cross-section area (k²). An ant scaled to elephant size would collapse."),
  CHECK("A 1:64 scale model truck is 9 inches long. The real truck is…", ["64 inches", "576 inches (48 ft)", "9 × 64² inches", "73 inches"], 1, "Lengths × 64: 9 × 64 = 576 in = 48 ft."),
  E("Area scaling", "A trailer floor plan drawn at 1:50 has an area of 6 square inches on paper. What's the real area in square inches?",
    ["Length scale k = 50.", "Area scale k² = 2,500.", "6 × 2,500 = 15,000 in²."], "**15,000 in²**, about 104 ft². Forgetting to square the scale factor is the number one mistake here."),
  N("Common traps", "- **Matching the wrong sides.** Line up corresponding vertices first (the order in △ABC ≅ △DEF tells you A↔D, B↔E, C↔F).\n- **SSA and AAA aren't congruence shortcuts.**\n- **Scaling area by k instead of k².**\n- **Congruent figures are similar** (k = 1), but similar figures usually aren't congruent.")
 ],
 "practice": [
  MC("Which is **not** a valid congruence shortcut?", ["SSS", "SAS", "SSA", "ASA"], 2, "Two different triangles can fit SSA."),
  MC("Similar figures have…", ["equal sides", "equal angles and proportional sides", "equal areas", "equal perimeters"], 1, "Same shape, scaled."),
  MC("△ABC ≅ △XYZ. Which side equals BC?", ["XY", "YZ", "XZ", "AB"], 1, "B↔Y, C↔Z."),
  NUM("Two similar triangles: sides 3, 4, 5 and the bigger one's shortest side is 9. Its longest side?", 15, "k = 3. 5 × 3 = 15."),
  NUM("A 5 ft person has a 3 ft shadow. A tree's shadow is 27 ft. Tree height?", 45, "5/3 = h/27 → h = 45.", unit="ft"),
  NUM("Scale factor 3. Original area 10 cm². New area?", 90, "10 × 3² = 90.", unit="cm²"),
  NUM("Scale factor 2. Original volume 50 cm³. New volume?", 400, "50 × 2³ = 400.", unit="cm³"),
  MC("Two right triangles have equal hypotenuses and one equal leg. They're congruent by…", ["AAA", "HL", "SSA", "AA"], 1, "Hypotenuse-Leg."),
  NUM("Two similar trailers: the small one has a 12 ft length and 300 ft³ volume. The big one is 24 ft. Its volume?", 2400,
      "k = 2, volume × 2³ = 8: 300 × 8 = **2,400 ft³**. Double the length, eight times the space.",
      level="challenge", hint="Volume scales by k³.", unit="ft³"),
  NUM("Two similar triangles have areas 16 and 36. If the smaller has a side of 8, what's the matching side of the larger?", 12,
      "Area ratio 36/16 = 9/4 = k². So k = 3/2. 8 × 1.5 = **12**.",
      level="challenge", hint="Take the square root of the area ratio to get k."),
  MC("A map scale is 1 inch : 20 miles. A region is 3 in² on the map. Its real area is…", ["60 mi²", "400 mi²", "1,200 mi²", "8,000 mi²"], 2,
     "Area scale = 20² = 400. 3 × 400 = **1,200 mi²**.",
     level="challenge", hint="Square the length scale."),
  NUM("A 4 ft fence post casts a 6 ft shadow. A building casts a 90 ft shadow. How tall is the building?", 60,
      "4/6 = h/90 → h = 90 × 4 ÷ 6 = **60 ft**.",
      level="challenge", hint="Height to shadow is the same ratio for both.", unit="ft"),
 ],
 "sources": [GEO]})

# ---------------------------------------------------------------- Right-triangle trig
L.append({"id": "right-triangle-trigonometry", "title": "Right-triangle trigonometry", "band": "Grade 10", "minutes": 36,
 "lede": "Three ratios that let you find any side or angle of a right triangle. How engineers measure what they can't reach, and how a 6% road grade becomes an angle.",
 "sections": [
  T("## Name the sides from the angle\nIn a right triangle, pick one of the acute angles and call it **θ** (theta). Then:\n\n- **Hypotenuse**: the longest side, across from the right angle. It never changes.\n- **Opposite**: the side **across** from θ.\n- **Adjacent**: the side **next to** θ that isn't the hypotenuse.\n\nSwitch to the other acute angle and *opposite* and *adjacent* trade places."),
  FIG(TRI, "Opposite and adjacent depend on which angle you're working from. The hypotenuse is always across from the right angle."),
  T("## SOH CAH TOA\nBecause all right triangles with the same angle θ are **similar** (AA), these ratios depend only on θ, not on the triangle's size:\n\n| Ratio | Definition | Memory |\n|---|---|---|\n| **sine** | sin θ = opposite ÷ hypotenuse | **SOH** |\n| **cosine** | cos θ = adjacent ÷ hypotenuse | **CAH** |\n| **tangent** | tan θ = opposite ÷ adjacent | **TOA** |\n\nA calculator stores these ratios for every angle. (Make sure it's in **degree** mode.)"),
  E("Find a side", "A ramp makes a 30° angle with the ground and is 12 ft long. How high does it rise?",
    ["Known: hypotenuse = 12, angle = 30°. Want: opposite (height).", "Opposite and hypotenuse → **sine**.", "sin 30° = h ÷ 12 → h = 12 × sin 30° = 12 × 0.5 = 6."], "**6 ft.**"),
  E("Find an angle", "A road climbs 6 ft for every 100 ft of horizontal distance (a **6% grade**). What angle is that?",
    ["Opposite = 6, adjacent = 100 → **tangent**.", "tan θ = 6 ÷ 100 = 0.06.", "Use inverse tangent: θ = tan⁻¹(0.06) ≈ 3.4°."],
    "**About 3.4°.** It doesn't sound like much, but 6% is steep enough for runaway-truck ramps and *check your brakes* signs on long mountain descents."),
  CHECK("You know the adjacent side and the hypotenuse. Which ratio do you use?", ["sine", "cosine", "tangent", "Pythagorean theorem only"], 1, "**CAH**: cos = adjacent ÷ hypotenuse."),
  T("## Special right triangles\nTwo triangles show up so often you should know their ratios by heart:\n\n| Triangle | Side ratio | Where it comes from |\n|---|---|---|\n| **45°-45°-90°** | 1 : 1 : √2 | half a square, cut along the diagonal |\n| **30°-60°-90°** | 1 : √3 : 2 | half an equilateral triangle |\n\nIn the 30-60-90, the **shortest** side is across from 30°, the **√3** side is across from 60°, and the hypotenuse (2) is across from 90°.\n\nSo: **sin 30° = 1/2**, **cos 60° = 1/2**, **tan 45° = 1**, **sin 45° = cos 45° = √2/2 ≈ 0.707**."),
  T("## Angles of elevation and depression\n- **Angle of elevation**: looking **up** from horizontal.\n- **Angle of depression**: looking **down** from horizontal.\n\nThey're equal when two people look at each other (alternate interior angles with parallel horizontal lines).\n\n*You stand 50 m from a building and look up 40° to the top.* Height = 50 × tan 40° ≈ 50 × 0.839 ≈ **42 m**. You just measured a building without touching it. Surveyors do this every day."),
  N("Common traps", "- **Calculator in radian mode.** sin 30 in radians is −0.988, not 0.5. Check the mode.\n- **Mislabeling opposite and adjacent.** Always label from the angle you're using.\n- **Using trig on non-right triangles.** SOH CAH TOA only works with a 90° angle (other triangles use the laws of sines and cosines, in later courses).\n- **sin⁻¹ isn't 1/sin.** It's the **inverse**: it takes a ratio and gives back the angle.")
 ],
 "practice": [
  MC("tan θ =", ["opposite ÷ hypotenuse", "adjacent ÷ hypotenuse", "opposite ÷ adjacent", "adjacent ÷ opposite"], 2, "TOA."),
  NUM("sin 30° = ?", 0.5, "Half of the hypotenuse, from the 30-60-90 triangle.", tol=0.001),
  NUM("tan 45° = ?", 1, "Opposite = adjacent in a 45-45-90."),
  NUM("Hypotenuse 20, angle 30°. Find the side opposite the 30° angle.", 10, "20 × sin 30° = 10."),
  NUM("A 45-45-90 triangle has legs of 7. Its hypotenuse, to 2 decimals?", 9.9, "7√2 ≈ 9.90.", tol=0.01),
  NUM("A 30-60-90 triangle's short leg is 5. Its hypotenuse?", 10, "Hypotenuse = 2 × short leg."),
  MC("Looking up from the ground to a plane is an angle of…", ["depression", "elevation", "inclination only", "reflection"], 1, "Up from horizontal."),
  NUM("Opposite = 8, adjacent = 15. What is tan θ? (3 decimals)", 0.533, "8 ÷ 15 ≈ 0.533.", tol=0.001),
  NUM("A ladder 20 ft long leans against a wall at 70° to the ground. How high does it reach? (1 decimal; sin 70° ≈ 0.940)", 18.8,
      "Opposite to the angle = height. 20 × 0.940 = **18.8 ft**.",
      level="challenge", hint="You have the hypotenuse and want the opposite side.", tol=0.06, unit="ft"),
  NUM("A road rises 8 ft over 100 ft of horizontal distance. To the nearest tenth of a degree, what's the angle? (tan⁻¹(0.08) ≈ ?)", 4.6,
      "tan θ = 0.08 → θ = tan⁻¹(0.08) ≈ **4.6°**. That's an 8% grade.",
      level="challenge", hint="Use inverse tangent.", tol=0.06, unit="°",
      steps=["Opposite = 8, adjacent = 100.", "tan θ = 0.08.", "θ = tan⁻¹(0.08) ≈ 4.57° ≈ 4.6°."]),
  NUM("From a 60 m cliff, the angle of depression to a boat is 30°. How far is the boat from the base of the cliff? (Nearest meter; tan 30° ≈ 0.577)", 104,
      "The angle of elevation from the boat is also 30°. tan 30° = 60 ÷ d → d = 60 ÷ 0.577 ≈ **104 m** (exactly 60√3).",
      level="challenge", hint="Depression from the top = elevation from the boat.", tol=1, unit="m"),
  MC("Why do sin, cos and tan depend only on the angle, not the triangle's size?", ["Calculators define them that way", "All right triangles with that angle are similar, so their side ratios are equal", "Bigger triangles have bigger angles", "They don't: they depend on size"], 1,
     "AA similarity: same right angle plus same θ → same shape → same ratios. This is the idea the whole subject rests on.",
     level="challenge", hint="Think back to the last lesson."),
 ],
 "sources": [AT, {"title": "OpenStax, Algebra and Trigonometry 2e, 7.2 Right Triangle Trigonometry", "url": "https://openstax.org/books/algebra-and-trigonometry-2e/pages/7-2-right-triangle-trigonometry"}]})

# ---------------------------------------------------------------- Coordinate geometry
L.append({"id": "coordinate-geometry", "title": "Coordinate geometry", "band": "Grade 10", "minutes": 32,
 "lede": "Put shapes on a grid and geometry turns into algebra. Distance, midpoints, proving a shape is a rectangle with nothing but numbers, and the equation of a circle.",
 "sections": [
  T("## The distance formula\nThe distance between (x₁, y₁) and (x₂, y₂) is:\n\n**d = √((x₂ − x₁)² + (y₂ − y₁)²)**\n\nIt's just the **Pythagorean theorem**: the horizontal change and the vertical change are the legs of a right triangle, and the distance is the hypotenuse."),
  E("Distance", "Find the distance from (1, 2) to (7, 10).", ["Horizontal change: 7 − 1 = 6.", "Vertical change: 10 − 2 = 8.", "d = √(36 + 64) = √100 = 10."], "**10.** (A 6-8-10 triangle: a 3-4-5 doubled.)"),
  T("## The midpoint formula\nThe midpoint is the **average** of the x's and the average of the y's:\n\n**M = ((x₁ + x₂) ÷ 2, (y₁ + y₂) ÷ 2)**\n\nMidpoint of (2, 8) and (10, 4): ((2 + 10) ÷ 2, (8 + 4) ÷ 2) = **(6, 6)**."),
  CHECK("Midpoint of (−4, 3) and (6, 9)?", ["(1, 6)", "(2, 12)", "(5, 3)", "(10, 6)"], 0, "(−4 + 6) ÷ 2 = 1; (3 + 9) ÷ 2 = 6."),
  T("## Proving shapes with algebra\nThree tools do almost everything:\n\n| To show… | Use | Look for |\n|---|---|---|\n| sides are **equal** | distance | same lengths |\n| sides are **parallel** | slope | **equal** slopes |\n| sides are **perpendicular** | slope | slopes multiply to **−1** |\n| diagonals **bisect** each other | midpoint | same midpoint |\n\n- **Parallelogram**: both pairs of opposite sides parallel (or diagonals share a midpoint).\n- **Rectangle**: a parallelogram with a right angle (perpendicular sides), or with equal diagonals.\n- **Rhombus**: all four sides equal.\n- **Square**: both a rectangle and a rhombus."),
  E("Is it a rectangle?", "Points A(0, 0), B(4, 2), C(3, 4), D(−1, 2).",
    ["Slopes: AB = 2/4 = 1/2. BC = 2/(−1) = −2. CD = (2 − 4)/(−1 − 3) = 1/2. DA = 2/(−1) = −2.", "AB ∥ CD and BC ∥ DA → parallelogram.", "AB × BC = (1/2)(−2) = −1 → perpendicular → right angle."],
    "**Yes, a rectangle.** Check: AB = √20, BC = √5, so it's not a square."),
  T("## The equation of a circle\nA circle is every point at distance **r** from a center (h, k). Write the distance formula with that idea and square both sides:\n\n**(x − h)² + (y − k)² = r²**\n\n- Center (3, −2), radius 5: **(x − 3)² + (y + 2)² = 25**\n- **x² + y² = 49**: center (0, 0), radius 7.\n\nWatch the signs: (y + 2) means k = **−2**."),
  CHECK("The circle (x + 1)² + (y − 4)² = 36 has center and radius…", ["(1, −4), 36", "(−1, 4), 6", "(−1, 4), 36", "(1, 4), 6"], 1, "x + 1 = x − (−1), so h = −1. k = 4. r = √36 = 6."),
  N("Common traps", "- **Subtracting coordinates in different orders** for slope. Keep (y₂ − y₁) and (x₂ − x₁) in the same order.\n- **Forgetting the square root** in the distance formula.\n- **Circle signs:** (x − h) means a **plus** h in the center if you see a minus, and vice versa.\n- **Using r² as the radius.** The right side is r²; take the square root.")
 ],
 "practice": [
  NUM("Distance from (0, 0) to (3, 4)?", 5, "√(9 + 16) = 5."),
  NUM("Distance from (2, −1) to (8, 7)?", 10, "√(36 + 64) = 10."),
  MC("Midpoint of (4, 10) and (8, −2)?", ["(6, 4)", "(12, 8)", "(2, 6)", "(6, 6)"], 0, "(12 ÷ 2, 8 ÷ 2)."),
  MC("Slopes 3/4 and −4/3 are…", ["parallel", "perpendicular", "equal", "neither"], 1, "Product = −1."),
  MC("Center of (x − 5)² + (y + 3)² = 16?", ["(5, −3)", "(−5, 3)", "(5, 3)", "(−5, −3)"], 0, "Signs flip from the equation."),
  NUM("Radius of x² + y² = 81?", 9, "√81."),
  MC("A quadrilateral's diagonals have the same midpoint. It must be a…", ["square", "parallelogram", "trapezoid", "kite"], 1, "Diagonals bisecting each other is the parallelogram test."),
  MC("Equation of the circle with center (0, 2) and radius 3:", ["x² + (y − 2)² = 9", "x² + (y + 2)² = 9", "x² + (y − 2)² = 3", "(x − 2)² + y² = 9"], 0, "h = 0, k = 2, r² = 9."),
  NUM("M(3, 5) is the midpoint of AB, and A = (1, 1). What is the y-coordinate of B?", 9,
      "(1 + y) ÷ 2 = 5 → y = **9**. (And x: (1 + x) ÷ 2 = 3 → x = 5, so B = (5, 9).)",
      level="challenge", hint="Set up the midpoint formula and solve for the unknown endpoint."),
  MC("Is the point (6, 8) on the circle x² + y² = 100?", ["Yes", "No, it's inside", "No, it's outside", "Can't tell"], 0,
     "36 + 64 = 100 ✓. It sits exactly on the circle.",
     level="challenge", hint="Plug it in."),
  NUM("A truck drives from a depot at (0, 0) to (30, 40) on a map grid in miles, then to (30, 0). Total straight-line miles driven?", 90,
      "First leg: √(900 + 1,600) = 50. Second leg: straight down, 40. Total **90 miles**.",
      level="challenge", hint="Find each leg's distance, then add.", unit="miles"),
  MC("Points P(1, 1), Q(4, 5), R(8, 2), S(5, −2). The shape is a…", ["rectangle but not a square", "square", "rhombus but not a square", "trapezoid"], 1,
     "PQ: slope 4/3, length 5. QR: slope −3/4, length 5. RS: 4/3, 5. SP: −3/4, 5. All sides equal **and** adjacent sides perpendicular → **square**.",
     level="challenge", hint="Check all four slopes and all four lengths."),
 ],
 "sources": [AT, GEO]})

# ---------------------------------------------------------------- Circle theorems
L.append({"id": "circle-theorems", "title": "Circle theorems", "band": "Grade 10", "minutes": 34,
 "lede": "Arcs, chords, tangents and the surprising rules that connect their angles. Plus arc length and sector area, the math of tire wear and pizza slices.",
 "sections": [
  T("## Parts of a circle\n| Part | Meaning |\n|---|---|\n| **radius** | center to the edge |\n| **diameter** | edge to edge through the center (2 radii) |\n| **chord** | any segment with both ends on the circle (the diameter is the longest) |\n| **secant** | a line that cuts through the circle at two points |\n| **tangent** | a line that **touches** the circle at exactly one point |\n| **arc** | a piece of the circle's edge |\n| **sector** | a pizza-slice region between two radii |"),
  T("## Central and inscribed angles\nA **central angle** has its vertex at the **center**. Its measure **equals** the arc it cuts off: a 80° central angle cuts an 80° arc.\n\nAn **inscribed angle** has its vertex **on the circle**. Its measure is **half** the arc it cuts off.\n\n**Inscribed angle = ½ × intercepted arc**"),
  FIG(CIRC, "The central angle and the inscribed angle cut off the same arc. The inscribed one is exactly half."),
  T("## Three consequences\n1. **Inscribed angles on the same arc are equal.** Every point P on the far side sees AB at the same angle.\n2. **An angle inscribed in a semicircle is 90°.** The arc is 180°, half of that is 90°. (Thales' theorem: any triangle drawn with the diameter as one side and its third corner on the circle is a right triangle.)\n3. **Opposite angles of a quadrilateral inscribed in a circle add to 180°.** Together they intercept the whole 360° circle, and half of 360° is 180°."),
  CHECK("An inscribed angle intercepts a 110° arc. The angle is…", ["110°", "220°", "55°", "70°"], 2, "Half the arc."),
  T("## Tangent facts\n- A tangent is **perpendicular to the radius** at the point where it touches.\n- Two tangents drawn from the same outside point are **equal in length**.\n\nThe first one makes many problems into right triangles, and then the Pythagorean theorem finishes them.\n\n*A tangent from point P touches a circle of radius 5. P is 13 from the center. How long is the tangent segment?* The radius meets the tangent at 90°: 5² + t² = 13² → t = **12**."),
  T("## Arc length and sector area\nAn arc or sector is a **fraction** of the whole circle: **θ ÷ 360**.\n\n- **Arc length** = (θ ÷ 360) × 2πr\n- **Sector area** = (θ ÷ 360) × πr²\n\nA 90° arc on a circle of radius 10: (90 ÷ 360) × 2π(10) = ¼ × 62.83 ≈ **15.7**."),
  E("Tire math", "A truck tire has a diameter of about 40 inches. How far does the truck move in one full rotation, and how many rotations per mile?",
    ["One rotation = circumference = π × 40 ≈ 125.7 in.", "1 mile = 63,360 in.", "63,360 ÷ 125.7 ≈ 504."],
    "**≈126 inches per turn, about 504 turns per mile.** If worn tires shrink the diameter, the wheel turns more times per mile, and the speedometer, which counts rotations, reads a little **high**."),
  CHECK("A sector has a 60° angle in a circle of radius 6. Its area is…", ["6π", "12π", "36π", "2π"], 0, "(60/360) × π × 36 = ⅙ × 36π = 6π."),
  N("Common traps", "- **Inscribed vs central.** Center vertex = equal to the arc. Edge vertex = half the arc.\n- **Arc measure vs arc length.** Measure is in **degrees**; length is a **distance**. Two arcs can both be 60° and have very different lengths on different-size circles.\n- **Diameter vs radius** in formulas. Circumference = πd = 2πr. Area uses r.\n- **The tangent-radius right angle** is often unmarked. You're expected to know it.")
 ],
 "practice": [
  MC("A chord that passes through the center is a…", ["radius", "diameter", "tangent", "secant"], 1, "The longest chord."),
  NUM("Central angle 72°. Its intercepted arc?", 72, "Equal.", unit="°"),
  NUM("Inscribed angle intercepts a 140° arc. The angle?", 70, "Half.", unit="°"),
  NUM("An angle inscribed in a semicircle measures…", 90, "Half of 180°.", unit="°"),
  MC("A tangent and the radius at the point of tangency form…", ["a 45° angle", "a 90° angle", "a 180° angle", "any angle"], 1, "Always perpendicular."),
  NUM("Inscribed quadrilateral: one angle is 75°. Its opposite angle?", 105, "Opposite angles add to 180°.", unit="°"),
  NUM("Arc length of a 180° arc, radius 7? (Use π ≈ 3.14, 2 decimals.)", 21.98, "½ × 2π(7) = 7π ≈ 21.98.", tol=0.01),
  NUM("Two tangents from point P are drawn to a circle. One is 9 cm. The other is…", 9, "Tangents from the same point are equal.", unit="cm"),
  NUM("Tangent from P touches a circle of radius 8. P is 17 from the center. Tangent length?", 15,
      "Right angle at the tangent point: 8² + t² = 17² → t² = 289 − 64 = 225 → **t = 15**.",
      level="challenge", hint="Radius ⟂ tangent: Pythagorean theorem."),
  NUM("Sector with a 45° angle in a circle of radius 12. Area, to 1 decimal? (π ≈ 3.1416)", 56.5,
      "(45/360) × π × 144 = ⅛ × 144π = 18π ≈ **56.5**.",
      level="challenge", hint="Fraction of the circle × πr².", tol=0.06),
  NUM("Two inscribed angles intercept the same arc. One is 3x + 10, the other 5x − 20. Find x.", 15,
      "Inscribed angles on the same arc are equal: 3x + 10 = 5x − 20 → 30 = 2x → **x = 15** (each angle is 55°).",
      level="challenge", hint="They must be equal."),
  NUM("A 40-inch-diameter tire. About how many rotations does it make in 10 miles? (1 mile = 63,360 in; nearest hundred)", 5000,
      "Circumference ≈ 125.66 in. 633,600 ÷ 125.66 ≈ 5,042 → **about 5,000**.",
      level="challenge", hint="Total inches ÷ inches per rotation.", tol=100),
 ],
 "sources": [GEO, {"title": "OpenStax, Contemporary Mathematics, Ch. 10: Geometry", "url": "https://openstax.org/books/contemporary-mathematics/pages/10-introduction"}]})

save("math", L)
