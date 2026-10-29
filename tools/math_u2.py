from common import *
SRC = {"title": "Grade 7 standards overview (Common Core, via LibreTexts)", "url": "https://math.libretexts.org/Courses/Coalinga_College/Math_for_Educators_(MATH_010A_and_010B_CID120)/01%3A_Teaching_Elementary_Mathematics/1.04%3A_Common_Core_Standards_for_Mathematics/1.4.08%3A_Grade_7_Standards_Overview"}
L = []
L.append({"id": "variables-and-expressions", "title": "Variables and expressions", "band": "Grades 7–8", "minutes": 16,
 "lede": "Letters stand for numbers you don't know yet. Here's how to write, simplify and evaluate expressions.",
 "sections": [
  T("## Why letters?\nA **variable** is a letter that stands for a number that can change or that you don't know yet. If a load pays $2.10 per mile, the pay for m miles is **2.10m**. That's an **expression**: a math phrase with numbers, variables and operations, but no equals sign."),
  TERMS([("Term", "One piece of an expression, separated by + or −. In 3x + 5, the terms are 3x and 5."),
         ("Coefficient", "The number multiplying a variable. In 3x, it's 3."),
         ("Constant", "A term with no variable, like 5."),
         ("Like terms", "Terms with the same variable part: 4x and −x are like terms; 4x and 4x² are not.")]),
  T("## Evaluating\nTo **evaluate**, plug in the number and follow the order of operations (parentheses, exponents, multiply and divide left to right, add and subtract left to right).\n\nIf x = 4: 3x² − 2x + 1 = 3(16) − 8 + 1 = 41."),
  T("## Combining like terms\nAdd or subtract the coefficients of like terms. Leave unlike terms alone.\n\n5x + 3 − 2x + 7 = (5x − 2x) + (3 + 7) = **3x + 10**."),
  T("## The distributive property\nMultiply the outside number by **every** term inside: 4(x + 3) = 4x + 12.\n\nWatch negatives: −2(x − 5) = −2x + 10. The −2 hits the −5 too."),
  E("Simplify", "3(2x − 4) − (x − 7)",
    ["Distribute the 3: 6x − 12.", "Distribute the hidden −1: −x + 7.", "Combine: 6x − x = 5x, and −12 + 7 = −5."], "**5x − 5**"),
  E("Write an expression", "A driver earns a $150 base per day plus $0.55 per mile. Write daily pay for m miles, then find pay for 400 miles.",
    ["Pay = 150 + 0.55m.", "For m = 400: 150 + 0.55(400) = 150 + 220."], "**150 + 0.55m**, which is **$370** at 400 miles")
 ],
 "practice": [
  NUM("Evaluate 3x² − 2x + 1 when x = 4.", 41, "3(16) − 8 + 1."),
  MC("Simplify 5x + 3 − 2x + 7.", ["3x + 10", "7x + 10", "3x + 4", "13x"], 0, "Combine x terms and constants separately."),
  MC("Expand −2(x − 5).", ["−2x − 10", "−2x + 10", "2x − 10", "−2x − 5"], 1, "−2 × −5 = +10."),
  MC("Simplify 3(2x − 4) − (x − 7).", ["5x − 5", "5x − 19", "7x − 5", "5x + 3"], 0, "6x − 12 − x + 7."),
  MC("Which are like terms?", ["3x and 3y", "4x² and 4x", "−7ab and 2ab", "5 and 5x"], 2, "Same variable part: ab."),
  NUM("Pay is 150 + 0.55m. What's the pay for 600 miles?", 480, "150 + 330.", unit="dollars")
 ], "sources": [SRC]})

L.append({"id": "solving-one-and-two-step-equations", "title": "Solving one- and two-step equations", "band": "Grades 7–8", "minutes": 18,
 "lede": "An equation is a balance. Whatever you do to one side, do to the other, and the unknown falls out.",
 "sections": [
  T("## The balance idea\nAn **equation** says two expressions are equal: 3x + 5 = 20. Solving means finding the value of x that makes it true.\n\nThink of a balanced scale. You can do anything you like, as long as you do the **same thing to both sides**. The goal is to get x alone."),
  T("## Undo in reverse order\nTo isolate x, undo what was done to it, in the **opposite order**:\n\n1. Undo addition or subtraction first.\n2. Then undo multiplication or division.\n\nIt's like taking off shoes and socks: shoes come off first, because they went on last."),
  E("Two-step equation", "3x + 5 = 20",
    ["Undo +5: subtract 5 from both sides. 3x = 15.", "Undo ×3: divide both sides by 3. x = 5.", "Check: 3(5) + 5 = 20. ✓"], "**x = 5**"),
  E("With a fraction", "x/4 − 3 = 7",
    ["Add 3 to both sides: x/4 = 10.", "Multiply both sides by 4: x = 40.", "Check: 40/4 − 3 = 7. ✓"], "**x = 40**"),
  E("Real problem", "A load pays $1,450. Fuel costs $380 and the driver is paid $0.60 per mile. If the profit was $498, how many miles was the trip?",
    ["Profit = pay − fuel − driver: 1,450 − 380 − 0.60m = 498.", "Simplify: 1,070 − 0.60m = 498.", "Subtract 1,070: −0.60m = −572.", "Divide by −0.60: m ≈ 953."], "**About 953 miles**"),
  N("Always check", "Plug your answer back into the original equation. It takes ten seconds and catches most mistakes.")
 ],
 "practice": [
  NUM("Solve x + 17 = 42.", 25, "Subtract 17."),
  NUM("Solve 6x = 54.", 9, "Divide by 6."),
  NUM("Solve 3x + 5 = 20.", 5, "Subtract 5, divide by 3."),
  NUM("Solve x/4 − 3 = 7.", 40, "Add 3, multiply by 4."),
  NUM("Solve −2x + 9 = 1.", 4, "Subtract 9: −2x = −8. Divide by −2."),
  NUM("A gym charges $30 to join plus $25 a month. You've paid $280. How many months?", 10, "30 + 25m = 280 → 25m = 250.", unit="months")
 ], "sources": [SRC]})

L.append({"id": "multi-step-equations", "title": "Multi-step equations", "band": "Grade 8", "minutes": 20,
 "lede": "Variables on both sides, parentheses and fractions: one clean process handles them all.",
 "sections": [
  T("## The four-step process\n1. **Clear parentheses** with the distributive property.\n2. **Combine like terms** on each side.\n3. **Move variables to one side** (add or subtract a variable term from both sides).\n4. **Solve** the two-step equation that's left."),
  E("Variables on both sides", "5x − 7 = 2x + 8",
    ["Subtract 2x from both sides: 3x − 7 = 8.", "Add 7: 3x = 15.", "Divide by 3: x = 5."], "**x = 5**"),
  E("With parentheses", "4(x − 2) = 2(x + 3)",
    ["Distribute: 4x − 8 = 2x + 6.", "Subtract 2x: 2x − 8 = 6.", "Add 8: 2x = 14.", "x = 7."], "**x = 7**"),
  T("## Clearing fractions\nMultiply every term by the least common denominator. x/3 + x/2 = 10 → multiply by 6: 2x + 3x = 60 → 5x = 60 → x = 12."),
  T("## No solution or infinitely many\n- If the variables cancel and you get something **false** (like 5 = 9), there's **no solution**.\n- If they cancel and you get something **always true** (like 4 = 4), **every number** is a solution."),
  E("Break-even", "Company A charges $40 plus $1.50 per mile. Company B charges $100 plus $1.20 per mile. At how many miles do they cost the same?",
    ["Set equal: 40 + 1.5m = 100 + 1.2m.", "Subtract 1.2m: 40 + 0.3m = 100.", "Subtract 40: 0.3m = 60.", "m = 200."], "**200 miles.** Under that, A is cheaper; over it, B is.")
 ],
 "practice": [
  NUM("Solve 5x − 7 = 2x + 8.", 5, "3x = 15."),
  NUM("Solve 4(x − 2) = 2(x + 3).", 7, "4x − 8 = 2x + 6."),
  NUM("Solve x/3 + x/2 = 10.", 12, "Multiply by 6: 5x = 60."),
  NUM("Solve 3(2x + 1) − 4x = 11.", 4, "6x + 3 − 4x = 11 → 2x = 8."),
  MC("Solve 2(x + 3) = 2x + 6.", ["x = 0", "No solution", "Every number works", "x = 3"], 2, "Both sides are identical: 2x + 6 = 2x + 6."),
  MC("Solve 3x + 4 = 3x − 1.", ["x = 5", "No solution", "Every number works", "x = 0"], 1, "The x's cancel, leaving 4 = −1, which is false."),
  NUM("Plan A: $40 + $1.50/mile. Plan B: $100 + $1.20/mile. At how many miles are they equal?", 200, "0.3m = 60.", unit="miles")
 ], "sources": [SRC]})

L.append({"id": "inequalities", "title": "Inequalities", "band": "Grades 7–8", "minutes": 16,
 "lede": "Solving for a range of answers instead of one, and the one rule that trips everyone up.",
 "sections": [
  T("## Reading inequality signs\n| Sign | Meaning | Example |\n|---|---|---|\n| < | less than | x < 5 |\n| > | greater than | x > −2 |\n| ≤ | less than or equal to | x ≤ 10 |\n| ≥ | greater than or equal to | x ≥ 0 |\n\nThe open side of the sign faces the bigger number. \"At least\" means ≥. \"At most\" and \"no more than\" mean ≤."),
  T("## Solving\nSolve exactly like an equation, with **one exception**:\n\n**When you multiply or divide both sides by a negative number, flip the sign.**\n\nWhy? 2 < 5 is true. Multiply both by −1: −2 and −5. Now −2 is the **bigger** one, so the sign must flip: −2 > −5."),
  E("Flip the sign", "−3x + 4 ≥ 19",
    ["Subtract 4: −3x ≥ 15.", "Divide by −3 and flip: x ≤ −5."], "**x ≤ −5**"),
  T("## Graphing on a number line\nUse an **open circle** for < or > (the endpoint isn't included) and a **closed circle** for ≤ or ≥ (it is). Shade the direction of the solutions."),
  E("Word problem", "A truck can carry at most 45,000 lb of cargo. Pallets weigh 1,800 lb each. How many pallets can it carry?",
    ["1,800p ≤ 45,000.", "p ≤ 25."], "**At most 25 pallets**")
 ],
 "practice": [
  MC("Solve x + 8 > 3.", ["x > 11", "x > −5", "x < −5", "x < 11"], 1, "Subtract 8."),
  MC("Solve −3x + 4 ≥ 19.", ["x ≥ −5", "x ≤ −5", "x ≥ 5", "x ≤ 5"], 1, "Dividing by −3 flips the sign."),
  MC("\"You must be at least 21.\" As an inequality:", ["a > 21", "a ≥ 21", "a < 21", "a ≤ 21"], 1, "At least includes 21 itself."),
  MC("On a number line, x < 4 uses…", ["A closed circle at 4, shade left", "An open circle at 4, shade left", "An open circle at 4, shade right", "A closed circle at 4, shade right"], 1, "Strict inequality: open circle."),
  NUM("Pallets weigh 1,800 lb. The limit is 45,000 lb. What's the most pallets you can carry?", 25, "1,800p ≤ 45,000.", unit="pallets"),
  MC("Solve −x/2 < 6.", ["x < −12", "x > −12", "x > 12", "x < 12"], 1, "Multiply by −2 and flip.")
 ], "sources": [SRC]})

L.append({"id": "exponents-and-scientific-notation", "title": "Exponents and scientific notation", "band": "Grade 8", "minutes": 20,
 "lede": "Repeated multiplication, the exponent rules, and how scientists write huge and tiny numbers.",
 "sections": [
  T("## What an exponent means\n2⁵ means 2 × 2 × 2 × 2 × 2 = 32. The 2 is the **base**; the 5 is the **exponent**, telling you how many times to multiply the base by itself."),
  T("## The rules\n| Rule | Example | Why |\n|---|---|---|\n| aᵐ × aⁿ = aᵐ⁺ⁿ | x³ × x⁴ = x⁷ | 3 x's times 4 x's is 7 x's |\n| aᵐ ÷ aⁿ = aᵐ⁻ⁿ | x⁶ ÷ x² = x⁴ | Two x's cancel |\n| (aᵐ)ⁿ = aᵐⁿ | (x²)³ = x⁶ | Three groups of two |\n| a⁰ = 1 | 7⁰ = 1 | x³ ÷ x³ = 1 = x⁰ |\n| a⁻ⁿ = 1/aⁿ | 2⁻³ = 1/8 | Keep dividing by 2 |"),
  N("Common trap", "x² + x³ is **not** x⁵. The rules work for multiplying and dividing, not adding. You can't combine x² + x³ at all."),
  T("## Scientific notation\nWrite a number as (a number from 1 to just under 10) × (a power of 10).\n\n- 5,800,000 = 5.8 × 10⁶ (move the decimal 6 places left)\n- 0.00042 = 4.2 × 10⁻⁴ (move it 4 places right)\n\nBig numbers get positive exponents; tiny numbers get negative ones."),
  E("Multiply in scientific notation", "(3 × 10⁴) × (5 × 10³)",
    ["Multiply the front numbers: 3 × 5 = 15.", "Add the exponents: 10⁴ × 10³ = 10⁷.", "15 × 10⁷ isn't proper form, so rewrite: 1.5 × 10⁸."], "**1.5 × 10⁸**")
 ],
 "practice": [
  NUM("2⁵ = ?", 32, "2 × 2 × 2 × 2 × 2."),
  MC("x³ × x⁴ = ?", ["x¹²", "x⁷", "2x⁷", "x"], 1, "Add exponents."),
  MC("(x²)³ = ?", ["x⁵", "x⁶", "x⁸", "3x²"], 1, "Multiply exponents."),
  NUM("5⁰ = ?", 1, "Anything (except 0) to the zero power is 1."),
  NUM("2⁻³ as a decimal = ?", 0.125, "1/8."),
  MC("5,800,000 in scientific notation:", ["58 × 10⁵", "5.8 × 10⁶", "5.8 × 10⁵", "0.58 × 10⁷"], 1, "Decimal moves 6 places."),
  MC("(3 × 10⁴)(5 × 10³) = ?", ["15 × 10¹²", "1.5 × 10⁸", "8 × 10⁷", "1.5 × 10⁷"], 1, "15 × 10⁷ = 1.5 × 10⁸.")
 ], "sources": [SRC]})

L.append({"id": "square-roots-and-irrational-numbers", "title": "Square roots and irrational numbers", "band": "Grade 8", "minutes": 16,
 "lede": "Undoing a square, estimating roots in your head, and the numbers that never end.",
 "sections": [
  T("## Square roots\nThe **square root** of a number is what you square to get it. √49 = 7 because 7² = 49.\n\nPerfect squares to know cold: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225."),
  T("## Estimating\nTo estimate √50, find the perfect squares around it: 49 < 50 < 64, so √50 is between 7 and 8, very close to 7 (since 50 is right next to 49). √50 ≈ 7.07."),
  T("## Rational vs irrational\n- **Rational** numbers can be written as a fraction of integers: 3, −2/5, 0.75, 0.333… (= 1/3). Their decimals either stop or repeat.\n- **Irrational** numbers can't. Their decimals go on forever with no repeating pattern: √2 = 1.41421356…, π = 3.14159265…\n\nThe square root of any whole number that isn't a perfect square is irrational."),
  T("## Cube roots\n∛27 = 3 because 3³ = 27. Unlike square roots, cube roots of negatives work: ∛(−8) = −2."),
  E("Simplifying a root", "√72",
    ["Find the largest perfect square factor: 72 = 36 × 2.", "√72 = √36 × √2 = 6√2."], "**6√2** (about 8.49)")
 ],
 "practice": [
  NUM("√144 = ?", 12, "12² = 144."),
  MC("√50 is between…", ["5 and 6", "6 and 7", "7 and 8", "8 and 9"], 2, "49 < 50 < 64."),
  MC("Which is irrational?", ["0.75", "√16", "√3", "2/7"], 2, "3 isn't a perfect square."),
  MC("0.333… (repeating) is…", ["Irrational", "Rational, equal to 1/3", "Not a real number", "Equal to 0.3"], 1, "Repeating decimals are rational."),
  NUM("∛(−8) = ?", -2, "(−2)³ = −8."),
  MC("Simplify √72.", ["6√2", "8√9", "36√2", "2√6"], 0, "√36 × √2.")
 ], "sources": [SRC]})
save("math", L)
