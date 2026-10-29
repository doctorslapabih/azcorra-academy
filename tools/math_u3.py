from common import *
SRC = {"title": "OpenStax, Prealgebra 2e, Ch. 9: Math Models and Geometry", "url": "https://openstax.org/details/books/prealgebra-2e"}
L = []

L.append({"id": "angles-and-lines", "title": "Angles and lines", "band": "Grades 7–8", "minutes": 16,
 "lede": "Angles are measured turns. A handful of rules about straight lines and parallel lines solve most angle puzzles.",
 "sections": [
  T("## Measuring a turn\nAn **angle** is formed by two rays from a shared point (the **vertex**). It's measured in **degrees**: a full turn is 360°.\n\n| Name | Size |\n|---|---|\n| Acute | less than 90° |\n| Right | exactly 90° (the little square in the corner) |\n| Obtuse | between 90° and 180° |\n| Straight | exactly 180° |\n| Reflex | between 180° and 360° |"),
  T("## Angle pairs\n- **Complementary** angles add to **90°**.\n- **Supplementary** angles add to **180°**. Angles side by side on a straight line are supplementary.\n- **Vertical angles** are the opposite angles where two lines cross. They are always **equal**.\n- Angles all the way around a point add to **360°**."),
  T("## Parallel lines and a transversal\nWhen a line (the **transversal**) cuts across two parallel lines, it makes 8 angles but only **two different sizes**. Every angle is equal to one size or the other, and the two sizes add to 180°.\n\n- **Corresponding** angles (same position at each crossing) are equal.\n- **Alternate interior** angles (inside the parallels, opposite sides of the transversal, a Z shape) are equal.\n- **Co-interior** angles (inside, same side, a C shape) add to 180°."),
  T("## Triangles\nThe three angles of any triangle add to **180°**. Tear the corners off a paper triangle and line them up: they make a straight line.\n\nFor any polygon with n sides, the interior angles add to **(n − 2) × 180°**. A square: 2 × 180 = 360°. A hexagon: 4 × 180 = 720°."),
  E("Find the missing angle", "A triangle has angles 47° and 68°. What is the third?",
    ["Angles in a triangle add to 180°.", "180 − 47 − 68 = 65."], "**65°**"),
  E("Use a straight line", "Two lines cross. One angle is 112°. Find the other three.",
    ["The angle next to it is supplementary: 180 − 112 = 68°.", "Vertical angles are equal, so the opposite angles are 112° and 68°."], "**68°, 112°, 68°**"),
  N("Puzzle habit", "In an angle problem, label every angle you can find in one step, even if the question didn't ask for it. The answer is usually two or three easy steps chained together.")
 ],
 "practice": [
  NUM("What is the complement of 34°?", 56, "90 − 34.", unit="degrees"),
  NUM("What is the supplement of 125°?", 55, "180 − 125.", unit="degrees"),
  MC("Two lines cross. Vertical angles are…", ["Always equal", "Always supplementary", "Always 90°", "Equal only if the lines are parallel"], 0, "Opposite angles at a crossing match."),
  NUM("A triangle has angles 90° and 38°. Find the third.", 52, "180 − 90 − 38.", unit="degrees"),
  NUM("What do the interior angles of a pentagon (5 sides) add to?", 540, "(5 − 2) × 180.", unit="degrees"),
  MC("Parallel lines are cut by a transversal. One angle is 70°. Which sizes appear among the 8 angles?", ["Only 70°", "70° and 110°", "70°, 90° and 110°", "70° and 20°"], 1, "Only two sizes, and they add to 180°.")
 ], "sources": [SRC]})

L.append({"id": "area-and-perimeter", "title": "Area and perimeter", "band": "Grades 7–8", "minutes": 18,
 "lede": "Perimeter is the fence; area is the grass. Learn the core formulas and the trick for odd shapes.",
 "sections": [
  T("## Two different questions\n- **Perimeter** is the distance **around** a shape. Add up the side lengths. Units: feet, meters.\n- **Area** is the space **inside**. Units are squared: ft², m², because you're counting unit squares."),
  T("## The formulas\n| Shape | Area |\n|---|---|\n| Rectangle | length × width |\n| Square | side² |\n| Parallelogram | base × height |\n| Triangle | ½ × base × height |\n| Trapezoid | ½ × (base₁ + base₂) × height |\n\nThe **height** is always measured **straight up** (perpendicular to the base), not along a slanted side."),
  T("## Why the triangle is half\nAny triangle is exactly half of a parallelogram with the same base and height. Copy it, flip the copy, and the two fit together. That's where the ½ comes from."),
  T("## Odd shapes: split or subtract\nFor an L-shape or a room with a cutout, either **split** it into rectangles and add the areas, or draw the big rectangle around it and **subtract** the missing piece."),
  E("Composite shape", "An L-shaped floor: a 12 ft × 10 ft rectangle with a 4 ft × 5 ft corner cut out. Find the area.",
    ["Big rectangle: 12 × 10 = 120 ft².", "Cut-out: 4 × 5 = 20 ft².", "120 − 20 = 100."], "**100 ft²**"),
  E("Scaling trap", "You double every side of a square. What happens to the area?",
    ["A side of s has area s².", "A side of 2s has area (2s)² = 4s²."], "The area becomes **4 times** bigger, not 2 times."),
  N("Remember", "When you scale a shape by a factor k, perimeter scales by k but area scales by **k²**. This is why a 16-inch pizza has about 1.8 times the pizza of a 12-inch one.")
 ],
 "practice": [
  NUM("A rectangle is 9 m by 6 m. What is its perimeter?", 30, "2(9 + 6).", unit="m"),
  NUM("Find the area of a triangle with base 10 and height 7.", 35, "½ × 10 × 7."),
  NUM("A trapezoid has bases 8 and 12 and height 5. Area?", 50, "½ × (8 + 12) × 5."),
  NUM("A parallelogram has base 11 cm and height 4 cm. Its slanted side is 5 cm. Area?", 44, "Base × height. The slanted side is a distractor.", unit="cm²"),
  MC("You triple every side of a rectangle. The area becomes…", ["3 times bigger", "6 times bigger", "9 times bigger", "27 times bigger"], 2, "Area scales by 3² = 9."),
  NUM("A 20 ft × 15 ft yard has a 6 ft × 6 ft patio. How much area is grass?", 264, "300 − 36.", unit="ft²")
 ], "sources": [SRC]})

L.append({"id": "circles-and-pi", "title": "Circles and π", "band": "Grade 7", "minutes": 16,
 "lede": "Every circle hides the same number, π. With it you can find any circle's distance around and area.",
 "sections": [
  TERMS([("Radius (r)", "Distance from the center to the edge."),
         ("Diameter (d)", "Distance straight across through the center. d = 2r."),
         ("Circumference (C)", "The distance around the circle: its perimeter."),
         ("π (pi)", "The ratio C ÷ d, the same for every circle: about 3.14159. It's irrational, so its decimals never end or repeat.")]),
  T("## The two formulas\n- **Circumference:** C = πd = 2πr\n- **Area:** A = πr²\n\nThe most common mistake is using the diameter in the area formula. Area always uses the **radius**: halve the diameter first."),
  T("## Where πr² comes from\nCut a circle into many thin pizza slices and arrange them alternating point-up and point-down. They form a shape close to a rectangle: its height is r and its length is half the circumference, πr. Area ≈ πr × r = **πr²**."),
  E("Area from diameter", "A circular table is 6 ft across. What's its area?",
    ["Radius = 6 ÷ 2 = 3 ft.", "A = π × 3² = 9π.", "9 × 3.14159 ≈ 28.3."], "**9π ≈ 28.3 ft²**"),
  E("Distance traveled", "A wheel has radius 14 inches. How far does it roll in one full turn?",
    ["One turn rolls one circumference.", "C = 2π(14) = 28π ≈ 88."], "**About 88 inches**"),
  N("Leave it in π", "If a question says \"exact\" or \"in terms of π\", write 9π instead of 28.27. Exact answers avoid rounding errors in multi-step problems.")
 ],
 "practice": [
  NUM("A circle has radius 5. What is its diameter?", 10, "d = 2r."),
  NUM("Circumference of a circle with diameter 10, rounded to one decimal (use π ≈ 3.14159)?", 31.4, "π × 10.", tol=0.06),
  NUM("Area of a circle with radius 3, rounded to one decimal?", 28.3, "9π.", tol=0.06),
  MC("A pizza is 14 inches across. Which expression gives its area?", ["π × 14²", "π × 7²", "2π × 7", "π × 14"], 1, "Use the radius, 7."),
  MC("If you double a circle's radius, its area…", ["Doubles", "Triples", "Quadruples", "Stays the same"], 2, "Area depends on r², so 2² = 4."),
  NUM("A wheel's circumference is 88 in. About how many full turns does it make in 880 in?", 10, "880 ÷ 88.", unit="turns")
 ], "sources": [SRC]})

L.append({"id": "volume-and-surface-area", "title": "Volume and surface area", "band": "Grades 7–8", "minutes": 18,
 "lede": "Volume is how much a box holds; surface area is how much cardboard it takes. Prisms, cylinders, cones and spheres.",
 "sections": [
  T("## Volume = base × height\nFor any **prism** or **cylinder** (same shape all the way up), volume is the area of the base times the height.\n\n| Solid | Volume |\n|---|---|\n| Rectangular box | l × w × h |\n| Cube | s³ |\n| Cylinder | πr²h |\n| Triangular prism | (½bh of triangle) × length |\n\nUnits are **cubed**: in³, m³."),
  T("## Pointy shapes are one third\nA **cone** or **pyramid** holds exactly **one third** of the prism or cylinder with the same base and height.\n\n- Cone: V = ⅓πr²h\n- Pyramid: V = ⅓ × base area × h\n- Sphere: V = ⁴⁄₃πr³"),
  T("## Surface area\nSurface area is the total area of all the faces, the wrapping paper. Units are **squared**.\n\n- **Box:** 2(lw + lh + wh), three pairs of matching rectangles.\n- **Cylinder:** 2πr² (top and bottom) + 2πrh (the label, unrolled into a rectangle)."),
  E("Box", "A shipping box is 2 ft × 3 ft × 4 ft. Find the volume and surface area.",
    ["Volume: 2 × 3 × 4 = 24 ft³.", "Faces: 2×3 = 6, 2×4 = 8, 3×4 = 12.", "Surface area: 2(6 + 8 + 12) = 52 ft²."], "**24 ft³** and **52 ft²**"),
  E("Cylinder", "A can has radius 3 cm and height 10 cm. Volume?",
    ["V = πr²h = π × 9 × 10 = 90π.", "90 × 3.14159 ≈ 282.7."], "**90π ≈ 282.7 cm³**"),
  N("Scaling again", "Scale every length by k: surface area scales by k², volume by **k³**. Double the size of a box and it holds 8 times as much.")
 ],
 "practice": [
  NUM("Volume of a cube with side 5?", 125, "5³."),
  NUM("Volume of a box 4 × 5 × 6?", 120, "Multiply."),
  NUM("Surface area of a box 2 × 3 × 4?", 52, "2(6 + 8 + 12)."),
  MC("A cone and a cylinder have the same base and height. The cone holds…", ["The same", "Half as much", "One third as much", "Twice as much"], 2, "Cone = ⅓πr²h."),
  NUM("Volume of a cylinder with radius 2 and height 7, rounded to one decimal?", 88.0, "28π ≈ 87.96.", tol=0.1),
  MC("You double every dimension of a box. Its volume becomes…", ["2×", "4×", "6×", "8×"], 3, "2³ = 8.")
 ], "sources": [SRC]})

L.append({"id": "the-pythagorean-theorem", "title": "The Pythagorean theorem", "band": "Grade 8", "minutes": 18,
 "lede": "In every right triangle, a² + b² = c². It lets you find any distance you can't measure directly.",
 "sections": [
  T("## The rule\nIn a **right triangle**, the side across from the right angle is the **hypotenuse** (c). It's always the longest side. The other two are the **legs** (a and b).\n\n**a² + b² = c²**\n\nIt only works for right triangles."),
  T("## Why it's true\nBuild a big square with side a + b. Put four copies of the triangle inside, one in each corner. The space left in the middle is a tilted square of side c, area c². Rearrange the same four triangles and the leftover space becomes two squares, a² and b². Same big square, same four triangles, so the leftover areas match: **a² + b² = c²**."),
  T("## Triples worth memorizing\nWhole-number right triangles: **3-4-5**, **5-12-13**, **8-15-17**, **7-24-25**. Multiples work too: 6-8-10, 9-12-15. Spotting one saves a calculation."),
  E("Find the hypotenuse", "Legs are 6 and 8.",
    ["6² + 8² = 36 + 64 = 100.", "c = √100 = 10."], "**10** (a 3-4-5 triple, doubled)"),
  E("Find a leg", "A 13 ft ladder leans on a wall. Its foot is 5 ft from the wall. How high does it reach?",
    ["The ladder is the hypotenuse: 5² + h² = 13².", "25 + h² = 169, so h² = 144.", "h = 12."], "**12 ft**"),
  E("Distance on a grid", "How far is (1, 2) from (7, 10)?",
    ["Horizontal gap: 7 − 1 = 6. Vertical gap: 10 − 2 = 8.", "Distance = √(6² + 8²) = √100."], "**10 units**"),
  N("Is it a right triangle?", "Check whether the two shorter sides squared add up to the longest side squared. 9, 12, 15: 81 + 144 = 225 = 15². Yes. This is how builders square a corner: measure 3 ft one way, 4 ft the other, and the diagonal must be 5 ft.")
 ],
 "practice": [
  NUM("Legs 3 and 4. Hypotenuse?", 5, "9 + 16 = 25."),
  NUM("Legs 5 and 12. Hypotenuse?", 13, "25 + 144 = 169."),
  NUM("Hypotenuse 17, one leg 8. Other leg?", 15, "289 − 64 = 225."),
  NUM("Legs 1 and 1. Hypotenuse, to two decimals?", 1.41, "√2.", tol=0.006),
  MC("Which side lengths form a right triangle?", ["4, 5, 6", "6, 8, 10", "5, 6, 7", "2, 3, 4"], 1, "36 + 64 = 100."),
  NUM("Distance from (0, 0) to (9, 12)?", 15, "√(81 + 144) = √225.")
 ], "sources": [SRC]})

save("math", L)
