import json, os
OUT = os.path.join(os.path.dirname(__file__), "..", "data", "lessons", "math")
os.makedirs(OUT, exist_ok=True)
SRC_CC = {"title": "Grade 7 standards overview (Common Core, via LibreTexts)", "url": "https://math.libretexts.org/Courses/Coalinga_College/Math_for_Educators_(MATH_010A_and_010B_CID120)/01%3A_Teaching_Elementary_Mathematics/1.04%3A_Common_Core_Standards_for_Mathematics/1.4.08%3A_Grade_7_Standards_Overview"}
SRC_CA = {"title": "California Mathematics Framework, Grade 7", "url": "https://www.cde.ca.gov/Ci/ma/cf/documents/mathfwgrade7.pdf"}
def T(md): return {"type": "text", "md": md}
def N(label, md): return {"type": "note", "label": label, "md": md}
def E(title, problem, steps, answer): return {"type": "example", "title": title, "problem": problem, "steps": steps, "answer": answer}
def MC(q, options, answer, why): return {"type": "mc", "q": q, "options": options, "answer": answer, "why": why}
def NUM(q, answer, why, tol=0.001, unit=None):
    d = {"type": "num", "q": q, "answer": answer, "why": why, "tol": tol}
    if unit: d["unit"] = unit
    return d

L = []

L.append({"id": "integers-and-negative-numbers", "title": "Integers and negative numbers", "band": "Grade 7", "minutes": 18,
 "lede": "Numbers below zero follow a few simple rules. Learn them once and you'll never second-guess a sign again.",
 "sections": [
  T("## What a negative number is\nA negative number is a distance **below zero**. You already use them: a bank balance of −$40 means you owe $40, and −6°F is six degrees below zero.\n\nPicture a number line. Zero sits in the middle, positives go right, negatives go left. Every number has an **opposite** the same distance from zero on the other side: the opposite of 7 is −7, and the opposite of −3 is 3."),
  {"type": "terms", "terms": [
    {"term": "Integer", "def": "A whole number or its opposite: …, −3, −2, −1, 0, 1, 2, 3, …"},
    {"term": "Opposite", "def": "Same distance from zero, other side. 5 and −5 are opposites, and they add to 0."},
    {"term": "Absolute value", "def": "Distance from zero, always positive or zero. Written |−8| = 8."}]},
  T("## Adding\nThink of positives as money in and negatives as money out.\n\n- **Same signs:** add the sizes and keep the sign. −4 + (−6) = −10. Two bills make a bigger bill.\n- **Different signs:** subtract the smaller size from the larger, and keep the sign of the larger. −9 + 4 = −5, because you owe 9 and pay 4, so you still owe 5."),
  T("## Subtracting\nSubtracting a number is the same as **adding its opposite**. That one rule handles every case:\n\n- 8 − 11 = 8 + (−11) = −3\n- 5 − (−3) = 5 + 3 = 8\n- −2 − 7 = −2 + (−7) = −9\n\nWhy does subtracting a negative add? Taking away a debt makes you richer. If someone forgives a $3 debt, your balance goes **up** $3."),
  E("A temperature swing", "At 6 a.m. it was −7°F. By noon it was 12°F. How much did it rise?",
    ["Change = end − start.", "12 − (−7) = 12 + 7.", "= 19."], "It rose **19°F**."),
  T("## Multiplying and dividing\nThe size works like normal. Only the sign needs a rule:\n\n| Signs | Result | Example |\n|---|---|---|\n| same (+ × + or − × −) | positive | (−6)(−4) = 24 |\n| different (+ × −) | negative | 7 × (−3) = −21 |\n\nSame rule for division: −45 ÷ 9 = −5, and −45 ÷ (−9) = 5.\n\nFor a long string, **count the negatives**. An even count gives a positive answer; an odd count gives a negative one. (−1)(−2)(−3) has three negatives, so it's −6."),
  N("Watch the parentheses", "(−3)² means (−3) × (−3) = 9. But −3² means −(3 × 3) = −9: the square happens first, then the minus. Exponents grab only what they touch."),
  E("Order of operations with negatives", "Simplify −2 × (5 − 8)² + 10.",
    ["Parentheses first: 5 − 8 = −3.", "Exponent: (−3)² = 9.", "Multiply: −2 × 9 = −18.", "Add: −18 + 10 = −8."], "**−8**")
 ],
 "practice": [
  NUM("−7 + 12 = ?", 5, "Different signs: 12 − 7 = 5, and 12 is the bigger size, so it's positive."),
  NUM("−4 − 9 = ?", -13, "Add the opposite: −4 + (−9) = −13."),
  NUM("6 − (−5) = ?", 11, "Subtracting a negative adds: 6 + 5 = 11."),
  NUM("(−3) × (−8) = ?", 24, "Same signs give a positive."),
  NUM("−56 ÷ 7 = ?", -8, "Different signs give a negative."),
  NUM("(−2)³ = ?", -8, "(−2)(−2)(−2): three negatives, so the answer is negative."),
  MC("Which is greater?", ["−12", "−3", "They're equal", "Can't tell"], 1, "−3 is closer to zero, so it's further right on the number line and greater."),
  NUM("An account is at −$85. A $120 payment comes in, then a $60 charge. What's the balance?", -25, "−85 + 120 − 60 = 35 − 60 = −25.", unit="dollars")
 ],
 "sources": [SRC_CC]})

L.append({"id": "fractions-the-complete-toolkit", "title": "Fractions: the complete toolkit", "band": "Grade 7", "minutes": 22,
 "lede": "Simplifying, adding, multiplying and dividing fractions, plus why each rule works.",
 "sections": [
  T("## What a fraction means\nA fraction is a **division**: 3/4 means 3 ÷ 4. The bottom number (denominator) says how many equal pieces the whole is cut into. The top (numerator) says how many pieces you have.\n\nSo 3/4 of a pizza is 3 of 4 equal slices, and 3/4 of $200 is $200 cut into 4 parts ($50 each), times 3: $150."),
  T("## Equivalent fractions and simplifying\nMultiplying or dividing the top and bottom by the same number doesn't change the value: 1/2 = 2/4 = 50/100.\n\nTo **simplify**, divide top and bottom by their greatest common factor (GCF). 18/24: the GCF is 6, so 18/24 = 3/4."),
  T("## Adding and subtracting\nYou can only add pieces of the same size, so you need a **common denominator**.\n\n1. Find a common denominator (the least common multiple of the bottoms is easiest).\n2. Rewrite each fraction with that denominator.\n3. Add or subtract the tops. Keep the bottom.\n4. Simplify."),
  E("Adding unlike fractions", "2/3 + 3/4",
    ["The LCM of 3 and 4 is 12.", "2/3 = 8/12 and 3/4 = 9/12.", "8/12 + 9/12 = 17/12.", "As a mixed number: 17/12 = 1 5/12."], "**17/12**, or 1 5/12"),
  T("## Multiplying\nTop times top, bottom times bottom. No common denominator needed.\n\nShortcut: **cross-cancel** first. In 3/4 × 8/9, the 3 and 9 share a 3, and the 4 and 8 share a 4: (1/1) × (2/3) = 2/3. Smaller numbers, fewer mistakes.\n\n\"Of\" means multiply: 2/5 of 30 = 2/5 × 30 = 12."),
  T("## Dividing\n**Keep, change, flip:** keep the first fraction, change ÷ to ×, flip the second fraction.\n\n5/6 ÷ 2/3 = 5/6 × 3/2 = 15/12 = 5/4.\n\nWhy it works: dividing asks \"how many of these fit into that?\" How many halves fit into 3? Six. And 3 ÷ 1/2 = 3 × 2 = 6. Dividing by a fraction is the same as multiplying by its flip (its **reciprocal**)."),
  T("## Mixed numbers\nConvert to an improper fraction before multiplying or dividing: 2 2/3 = (2 × 3 + 2)/3 = 8/3."),
  E("Multiplying mixed numbers", "1 1/2 × 2 2/3",
    ["Convert: 1 1/2 = 3/2 and 2 2/3 = 8/3.", "Cross-cancel the 3s: (1/2) × (8/1).", "= 8/2 = 4."], "**4**"),
  N("Comparing fractions", "To compare 5/8 and 3/5, cross-multiply: 5 × 5 = 25 vs 3 × 8 = 24. The fraction whose numerator made the bigger product (5/8) is larger. Or convert both to decimals: 0.625 vs 0.6.")
 ],
 "practice": [
  MC("Simplify 18/24.", ["9/12", "3/4", "2/3", "6/8"], 1, "Divide top and bottom by the GCF, 6."),
  MC("1/2 + 1/3 = ?", ["2/5", "5/6", "1/6", "2/6"], 1, "3/6 + 2/6 = 5/6. Adding tops and bottoms (2/5) is the classic error."),
  MC("7/8 − 1/4 = ?", ["6/4", "5/8", "6/8", "3/4"], 1, "1/4 = 2/8, so 7/8 − 2/8 = 5/8."),
  NUM("2/5 of 15 = ?", 6, "15 ÷ 5 = 3, times 2 = 6."),
  NUM("3/4 ÷ 1/8 = ?", 6, "3/4 × 8/1 = 24/4 = 6. Six eighths fit into three quarters."),
  NUM("1 1/2 × 2 2/3 = ?", 4, "3/2 × 8/3 = 24/6 = 4."),
  MC("Which is larger, 5/8 or 3/5?", ["5/8", "3/5", "Equal", "Can't tell"], 0, "0.625 is more than 0.6."),
  NUM("A driver has finished 3/5 of a 450-mile route. How many miles are left?", 180, "Left = 2/5 of 450 = 180.", unit="miles")
 ],
 "sources": [SRC_CC]})

L.append({"id": "decimals-and-percents", "title": "Decimals and percents", "band": "Grade 7", "minutes": 20,
 "lede": "Converting between fractions, decimals and percents, and the multiplier trick for any price change.",
 "sections": [
  T("## Three ways to write the same number\nA fraction, a decimal and a percent can all mean the same amount. **Percent** means \"per hundred\": 35% = 35/100 = 0.35.\n\n| Fraction | Decimal | Percent |\n|---|---|---|\n| 1/2 | 0.5 | 50% |\n| 1/4 | 0.25 | 25% |\n| 3/4 | 0.75 | 75% |\n| 1/5 | 0.2 | 20% |\n| 1/8 | 0.125 | 12.5% |\n| 1/3 | 0.333… | 33.3% |\n\nMemorize this table. It makes estimates instant."),
  T("## Converting\n- **Percent → decimal:** move the decimal two places left. 7% = 0.07.\n- **Decimal → percent:** move it two places right. 0.425 = 42.5%.\n- **Fraction → decimal:** divide top by bottom. 3/8 = 3 ÷ 8 = 0.375.\n- **Decimal → fraction:** read it by place value, then simplify. 0.375 = 375/1000 = 3/8."),
  T("## Percent of a number\nTurn the percent into a decimal and multiply: 18% of 250 = 0.18 × 250 = 45.\n\nMental shortcut: 10% is the number with the decimal moved one place. Build everything else from that. 15% of 60: 10% is 6, 5% is 3, so 9."),
  T("## The multiplier method\nFor any increase or decrease, multiply by one number:\n\n- **Increase by p%:** multiply by (1 + p). Add 7% tax: × 1.07.\n- **Decrease by p%:** multiply by (1 − p). Take 25% off: × 0.75.\n\nThis gets the final price in one step instead of two."),
  E("Discount and tax", "A $64 item is 25% off, then 7% sales tax is added. What do you pay?",
    ["After the discount: 64 × 0.75 = 48.", "After tax: 48 × 1.07 = 51.36."], "**$51.36**"),
  T("## Percent change\nPercent change = (new − old) ÷ old.\n\nDivide by the **starting** number, always. A price going from $50 to $65 is a change of 15, and 15 ÷ 50 = 0.30, so a 30% increase."),
  E("Percent change", "Fuel was $3.20 a gallon and is now $3.68. What's the percent increase?",
    ["Change: 3.68 − 3.20 = 0.48.", "Divide by the old price: 0.48 ÷ 3.20 = 0.15."], "**15% increase**"),
  N("Multiplying decimals", "Multiply as whole numbers, then count the total decimal places in both factors. 0.6 × 0.4: 6 × 4 = 24, two decimal places total, so 0.24.")
 ],
 "practice": [
  MC("0.375 as a fraction in lowest terms is…", ["37/100", "3/8", "375/100", "3/5"], 1, "375/1000 simplifies by 125 to 3/8."),
  NUM("3/5 as a percent (number only)?", 60, "3 ÷ 5 = 0.6 = 60%.", unit="%"),
  NUM("18% of 250 = ?", 45, "0.18 × 250 = 45."),
  NUM("A price rises from $80 to $92. What's the percent increase?", 15, "12 ÷ 80 = 0.15.", unit="%"),
  NUM("A $120 jacket is 30% off. What's the sale price?", 84, "120 × 0.70 = 84.", unit="dollars"),
  NUM("0.6 × 0.4 = ?", 0.24, "24 with two decimal places."),
  NUM("1.25 × 48 = ?", 60, "1.25 is 1 and a quarter: 48 + 12 = 60."),
  MC("A stock drops 20%, then gains 20%. Overall it's…", ["Back to even", "Down 4%", "Up 4%", "Down 20%"], 1, "0.8 × 1.2 = 0.96, a 4% loss.")
 ],
 "sources": [SRC_CC]})

L.append({"id": "ratios-rates-and-unit-rates", "title": "Ratios, rates and unit rates", "band": "Grade 7", "minutes": 20,
 "lede": "Comparing quantities, finding the better deal, and converting units without memorizing anything.",
 "sections": [
  T("## Ratios\nA **ratio** compares two amounts. If a fleet has 6 box trucks and 4 vans, the ratio of trucks to vans is 6:4, which simplifies to **3:2**. You simplify ratios the same way as fractions.\n\nCareful with part vs whole. The ratio of trucks to **all vehicles** is 6:10, or 3:5, so trucks are 3/5 of the fleet."),
  T("## Rates and unit rates\nA **rate** is a ratio of two different units: 300 miles per 5 hours, $18 for 4 pounds.\n\nA **unit rate** is the amount for **one** of the second unit. Divide: 300 ÷ 5 = 60 miles per hour. $18 ÷ 4 = $4.50 per pound."),
  E("Which deal is better?", "Brand A: 3 lb for $7.47. Brand B: 5 lb for $11.95.",
    ["Unit price A: 7.47 ÷ 3 = $2.49 per lb.", "Unit price B: 11.95 ÷ 5 = $2.39 per lb."], "**Brand B** is cheaper per pound."),
  T("## Converting units\nMultiply by a fraction equal to 1, arranged so the unit you don't want cancels. This is called **dimensional analysis**, and it's how scientists and engineers convert anything.\n\n90 minutes × (1 hour / 60 minutes) = 1.5 hours. The minutes cancel because one is on top and one is on the bottom."),
  E("Fuel for a run", "A truck gets 6.5 miles per gallon. How many gallons for a 520-mile run?",
    ["We want gallons, so put gallons on top: 520 miles × (1 gallon / 6.5 miles).", "Miles cancel: 520 ÷ 6.5 = 80."], "**80 gallons**"),
  N("Ratio tables", "When you scale a ratio up or down, multiply both parts by the same number. A recipe with 3 cups flour to 2 cups sugar becomes 9 to 6 if you triple it.")
 ],
 "practice": [
  MC("Simplify the ratio 12:18.", ["6:9", "2:3", "3:2", "4:6"], 1, "Divide both by 6."),
  MC("A class has 14 boys and 16 girls. What fraction are boys?", ["14/16", "7/15", "7/8", "1/2"], 1, "14 out of 30 total = 7/15. Part-to-whole uses the total."),
  NUM("A truck covers 270 miles in 4.5 hours. What's the average speed?", 60, "270 ÷ 4.5 = 60.", unit="mph"),
  NUM("12 bottles cost $5.40. What's the price per bottle?", 0.45, "5.40 ÷ 12 = 0.45.", unit="dollars"),
  NUM("How many gallons is 8 quarts? (4 quarts = 1 gallon)", 2, "8 × (1/4) = 2."),
  NUM("A recipe uses 3 cups of flour for every 2 cups of sugar. How much sugar goes with 9 cups of flour?", 6, "Flour tripled, so sugar triples: 2 × 3 = 6.", unit="cups"),
  MC("Which is the better buy?", ["16 oz for $3.20", "24 oz for $4.56", "Same", "Can't tell"], 1, "$0.20/oz vs $0.19/oz."),
  NUM("A driver is paid $0.62 per mile. How much for a 1,150-mile week?", 713, "1,150 × 0.62 = 713.", unit="dollars")
 ],
 "sources": [SRC_CC]})

L.append({"id": "proportions-and-scaling", "title": "Proportions and scaling", "band": "Grade 7", "minutes": 20,
 "lede": "When two quantities grow together at a fixed rate, and how to spot when they don't.",
 "sections": [
  T("## Proportions\nA **proportion** says two ratios are equal: 2/5 = 6/15. To solve one with an unknown, **cross-multiply**:\n\nx/12 = 5/8 → 8x = 60 → x = 7.5."),
  T("## Proportional relationships\nTwo quantities are **proportional** when one is always the same multiple of the other: y = kx. The number k is the **constant of proportionality** (the unit rate).\n\nThree ways to spot one:\n\n1. **Table:** y ÷ x gives the same k in every row.\n2. **Graph:** a straight line through the origin (0, 0).\n3. **Equation:** y = kx, with nothing added on."),
  E("Find k from a table", "x: 2, 5, 8 · y: 7, 17.5, 28",
    ["7 ÷ 2 = 3.5", "17.5 ÷ 5 = 3.5", "28 ÷ 8 = 3.5", "Every ratio matches, so it's proportional."], "**k = 3.5**, so y = 3.5x"),
  T("## When it's not proportional\nA fixed starting fee breaks proportionality. A tow that costs $75 plus $4 a mile: 10 miles costs $115, but 20 miles costs $155, not double. The graph is a line that doesn't pass through zero. That's a **linear** relationship, which you'll study in Algebra 1."),
  T("## Scale drawings and maps\nA scale is a proportion. If a map says 1 inch = 25 miles, then 3.5 inches = 3.5 × 25 = 87.5 miles."),
  E("Planning fuel", "A truck burned 18 gallons on a 117-mile leg. At the same rate, how many gallons for 455 miles?",
    ["Set up: 18/117 = x/455.", "Cross-multiply: 117x = 18 × 455 = 8,190.", "x = 8,190 ÷ 117 = 70."], "**70 gallons**")
 ],
 "practice": [
  NUM("Solve: x/12 = 5/8", 7.5, "8x = 60, so x = 7.5."),
  NUM("y is proportional to x, and y = 10 when x = 4. What is k?", 2.5, "k = y ÷ x = 10 ÷ 4."),
  NUM("On a map, 1 cm = 50 km. Two cities are 7 cm apart. How far is that?", 350, "7 × 50.", unit="km"),
  MC("Which table is proportional?", ["x: 1, 2, 3 · y: 4, 8, 12", "x: 1, 2, 3 · y: 5, 7, 9", "x: 1, 2, 3 · y: 2, 4, 7", "x: 0, 1, 2 · y: 3, 4, 5"], 0, "4/1 = 8/2 = 12/3 = 4."),
  MC("A plumber charges $25 plus $10 an hour. Is the total cost proportional to hours?", ["Yes", "No, because of the $25 fee", "Only after 2 hours", "Yes, k = 10"], 1, "With a fixed fee, the graph doesn't go through (0, 0)."),
  NUM("A truck burns 18 gallons per 117 miles. How many gallons for 455 miles?", 70, "117/18 = 6.5 mpg, and 455 ÷ 6.5 = 70.", unit="gallons"),
  NUM("A photo is 4 in by 6 in. It's enlarged so the short side is 10 in. How long is the long side?", 15, "Scale factor 10/4 = 2.5, and 6 × 2.5 = 15.", unit="in")
 ],
 "sources": [SRC_CC, SRC_CA]})

for l in L:
    json.dump(l, open(os.path.join(OUT, l["id"] + ".json"), "w"), ensure_ascii=False, indent=1)
print([l["id"] for l in L])
