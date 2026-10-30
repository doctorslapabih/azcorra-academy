from common import *

PC = {"title": "OpenStax, Precalculus 2e", "url": "https://openstax.org/details/books/precalculus-2e"}
AT = {"title": "OpenStax, Algebra and Trigonometry 2e", "url": "https://openstax.org/details/books/algebra-and-trigonometry-2e"}
C1 = {"title": "OpenStax, Calculus Volume 1", "url": "https://openstax.org/details/books/calculus-volume-1"}
L = []


def FIG(svg, caption): return {"type": "figure", "svg": svg, "caption": caption}


UNIT = """<svg viewBox="0 0 550 300" width="100%" style="max-width:600px" role="img" aria-label="Unit circle with key first-quadrant angles">
<g font-family="inherit" font-size="13" fill="currentColor" transform="translate(60,0)">
<line x1="40" y1="150" x2="300" y2="150" stroke="currentColor" stroke-opacity=".4"/>
<line x1="170" y1="20" x2="170" y2="280" stroke="currentColor" stroke-opacity=".4"/>
<circle cx="170" cy="150" r="120" fill="none" stroke="currentColor" stroke-width="2"/>
<line x1="170" y1="150" x2="273.9" y2="90" stroke="currentColor"/>
<line x1="170" y1="150" x2="254.9" y2="65.1" stroke="currentColor"/>
<line x1="170" y1="150" x2="230" y2="46.1" stroke="currentColor"/>
<circle cx="273.9" cy="90" r="3.5"/><circle cx="254.9" cy="65.1" r="3.5"/><circle cx="230" cy="46.1" r="3.5"/>
<circle cx="290" cy="150" r="3.5"/><circle cx="170" cy="30" r="3.5"/>
<text x="296" y="145">(1, 0)  0</text>
<text x="176" y="24">(0, 1)  π/2</text>
<text x="280" y="88">30° = π/6 → (√3/2, 1/2)</text>
<text x="262" y="62">45° = π/4 → (√2/2, √2/2)</text>
<text x="236" y="40">60° = π/3 → (1/2, √3/2)</text>
<text x="44" y="145" text-anchor="end">(−1, 0)  π</text>
<text x="176" y="292">(0, −1)  3π/2</text>
<text x="-50" y="292" fill-opacity=".7">every point = (cos θ, sin θ)</text>
</g></svg>"""

# ---------------------------------------------------------------- Unit circle and radians
L.append({"id": "the-unit-circle-and-radians", "title": "The unit circle and radians", "band": "Grades 11–12", "minutes": 36,
 "lede": "Trigonometry beyond right triangles. Radians, the natural way to measure angles, and the unit circle, which defines sine and cosine for any angle at all, even negative ones and angles past 360°.",
 "sections": [
  T("## Radians\nDegrees are arbitrary (360 probably comes from ancient Babylonian astronomy). **Radians** come from the circle itself:\n\n**One radian** is the angle that cuts off an arc **equal in length to the radius**.\n\nA full circle's circumference is 2πr, so a full turn is **2π radians**.\n\n| Degrees | Radians |\n|---|---|\n| 360° | 2π |\n| 180° | π |\n| 90° | π/2 |\n| 60° | π/3 |\n| 45° | π/4 |\n| 30° | π/6 |\n\n**Convert:** degrees × π/180 = radians; radians × 180/π = degrees. One radian ≈ **57.3°**."),
  T("## Why radians: arc length\nIn radians, **arc length s = rθ**. No conversion factor.\n\n*A truck tire with radius 0.5 m turns through 10 radians.* The truck moves s = 0.5 × 10 = **5 m**.\n\nAnd **linear speed v = rω** (ω in radians per second). Calculus formulas for sine and cosine only work cleanly in radians, which is why every math and physics course after this one uses them."),
  CHECK("Convert 120° to radians.", ["π/3", "2π/3", "3π/4", "4π/3"], 1, "120 × π/180 = 2π/3."),
  T("## The unit circle\nThe **unit circle** has radius 1, centered at the origin. Start at (1, 0) and rotate counterclockwise by angle θ. The point you land on is:\n\n**(cos θ, sin θ)**\n\nThat's the new **definition** of sine and cosine: the x- and y-coordinates on the unit circle. For acute angles it matches SOH CAH TOA (the hypotenuse is 1), but now it works for **any** angle."),
  FIG(UNIT, "The first-quadrant key angles. The other quadrants mirror these with sign changes."),
  T("## Signs by quadrant\n| Quadrant | Angles | cos (x) | sin (y) | tan |\n|---|---|---|---|---|\n| I | 0 to π/2 | + | + | + |\n| II | π/2 to π | − | + | − |\n| III | π to 3π/2 | − | − | + |\n| IV | 3π/2 to 2π | + | − | − |\n\nMemory: **All Students Take Calculus**: **A**ll positive in I, **S**ine in II, **T**angent in III, **C**osine in IV.\n\n**Reference angle:** the acute angle to the x-axis. Find the values for the reference angle, then apply the quadrant's signs.\n\n*cos 150°:* reference angle 30°, cos 30° = √3/2, quadrant II → cosine negative → **−√3/2**."),
  CHECK("sin 210° = ?", ["1/2", "−1/2", "√3/2", "−√3/2"], 1, "Reference 30°; quadrant III, sine negative."),
  T("## The Pythagorean identity\nEvery point on the unit circle satisfies x² + y² = 1. So for every angle:\n\n**sin²θ + cos²θ = 1**\n\nIf sin θ = 3/5 and θ is in quadrant II: cos²θ = 1 − 9/25 = 16/25, so cos θ = **−4/5** (negative in II)."),
  T("## Angles beyond one turn\nAngles **coterminal** with θ (ending in the same place) differ by full turns: θ ± 2π, θ ± 4π, …\n\n- 390° = 360° + 30°, so sin 390° = sin 30° = 1/2.\n- −π/2 (rotating **clockwise** a quarter turn) lands at (0, −1), same as 3π/2.\n\nThis repeating behavior is what makes sine and cosine perfect for anything that **cycles**: tides, seasons, sound, alternating current."),
  N("Common traps", "- **Calculator mode.** Radians vs degrees changes every answer.\n- **cos is x, sin is y.** Alphabetical: (c, s) ↔ (x, y).\n- **Signs come from the quadrant**, values from the reference angle.\n- **Radians are just numbers.** sin(2) means 2 radians, about 114.6°.")
 ],
 "practice": [
  MC("90° in radians is…", ["π", "π/2", "π/4", "2π"], 1, "90 × π/180."),
  NUM("π/3 radians in degrees?", 60, "180 ÷ 3.", unit="°"),
  NUM("1 radian is about how many degrees? (1 decimal)", 57.3, "180 ÷ π ≈ 57.3.", tol=0.06, unit="°"),
  MC("On the unit circle, the point at angle θ is…", ["(sin θ, cos θ)", "(cos θ, sin θ)", "(tan θ, 1)", "(θ, 1)"], 1, "x = cos, y = sin."),
  NUM("cos 0 = ?", 1, "Point (1, 0)."),
  NUM("sin(π/2) = ?", 1, "Point (0, 1)."),
  MC("In quadrant III, which is positive?", ["sine", "cosine", "tangent", "none"], 2, "Tangent = sin/cos = (−)/(−)."),
  NUM("Arc length on a circle of radius 4 for an angle of 2.5 radians?", 10, "s = rθ.", unit="units"),
  MC("cos(2π/3) = ?", ["1/2", "−1/2", "√3/2", "−√3/2"], 1,
     "2π/3 = 120°, reference angle 60°, quadrant II → cos negative: **−1/2**.",
     level="challenge", hint="Find the reference angle and the quadrant."),
  MC("sin θ = −5/13 and θ is in quadrant IV. cos θ = ?", ["12/13", "−12/13", "5/12", "−5/12"], 0,
     "cos²θ = 1 − 25/169 = 144/169 → cos θ = ±12/13. Quadrant IV: cosine positive → **12/13**.",
     level="challenge", hint="Pythagorean identity, then choose the sign."),
  NUM("A wheel of radius 0.5 m spins at 40 rad/s. Speed of the vehicle (no slipping)?", 20,
      "v = rω = 0.5 × 40 = **20 m/s** (about 45 mph).",
      level="challenge", hint="v = rω.", unit="m/s"),
  MC("sin(13π/6) = ?", ["−1/2", "1/2", "√3/2", "0"], 1,
     "13π/6 = 2π + π/6: coterminal with π/6. sin(π/6) = **1/2**.",
     level="challenge", hint="Subtract a full turn."),
 ],
 "sources": [PC, {"title": "OpenStax, Precalculus 2e, 5.2 Unit Circle: Sine and Cosine Functions", "url": "https://openstax.org/books/precalculus-2e/pages/5-2-unit-circle-sine-and-cosine-functions"}]})

# ---------------------------------------------------------------- Graphs of trig functions
L.append({"id": "graphs-of-trig-functions", "title": "Graphs of trig functions", "band": "Grades 11–12", "minutes": 34,
 "lede": "Waves. How amplitude, period, phase shift and midline let you model anything that repeats: tides, daylight hours, sound and the alternating current in every outlet.",
 "sections": [
  T("## The basic waves\nPlot sin x for x from 0 to 2π and you get one full wave: starts at 0, rises to 1 at π/2, back to 0 at π, down to −1 at 3π/2, back to 0 at 2π. Then it repeats forever.\n\n| | y = sin x | y = cos x |\n|---|---|---|\n| starts at (x = 0) | 0 (middle) | 1 (top) |\n| max / min | 1 / −1 | 1 / −1 |\n| period | 2π | 2π |\n\nThe cosine graph is the sine graph **shifted left by π/2**. They're the same wave, starting at different points in the cycle."),
  T("## The general form\n**y = A sin(B(x − C)) + D** (same for cosine)\n\n| Parameter | Controls | Formula |\n|---|---|---|\n| **A** | **amplitude**: height from midline to peak | amplitude = size of A (ignore sign); negative A flips the wave |\n| **B** | how fast it cycles | **period = 2π ÷ B** |\n| **C** | **phase shift**: horizontal slide | right by C |\n| **D** | **midline**: vertical shift | the wave centers on y = D |\n\n*y = 3 sin(2x) + 1:* amplitude 3, period 2π/2 = π, midline y = 1. It swings from **−2 to 4**."),
  CHECK("The period of y = sin(4x) is…", ["4π", "π/2", "2π", "π/4"], 1, "2π ÷ 4 = π/2."),
  T("## Frequency\n**Frequency** is how many cycles per unit time: **frequency = 1 ÷ period**.\n\nU.S. household electricity alternates at **60 Hz**: 60 full cycles per second, so each cycle takes 1/60 s. The voltage is literally a sine wave. Musical notes are too: the A above middle C is tuned to 440 Hz."),
  E("Model daylight hours", "Suppose a city's daylight averages 12 hours, swings 2 hours above and below over a year (365 days), and peaks around day 172 (late June). Write a model.",
    ["Midline D = 12. Amplitude A = 2.", "Period 365 → B = 2π ÷ 365.", "A cosine starts at its peak, so shift it to the peak day: C = 172.", "**h(t) = 2 cos((2π/365)(t − 172)) + 12**"],
    "Plug in t = 172: cos(0) = 1 → 14 hours (the longest day). Half a year later, about 10 hours. The same recipe models tides, temperatures and seasonal sales."),
  T("## Tangent\n**tan x = sin x ÷ cos x.** Where cos x = 0 (at π/2, 3π/2, …) tangent is undefined, so its graph has **vertical asymptotes** there.\n\n- Period: **π** (not 2π)\n- No amplitude: it runs from −∞ to +∞ between each pair of asymptotes"),
  CHECK("y = −2 cos x + 5 has a maximum value of…", ["2", "3", "5", "7"], 3, "Midline 5, amplitude 2: range 3 to 7."),
  T("## Reading a wave from a graph\n1. **Midline**: halfway between max and min: D = (max + min) ÷ 2.\n2. **Amplitude**: A = (max − min) ÷ 2.\n3. **Period**: distance from one peak to the next. Then B = 2π ÷ period.\n4. **Phase shift**: where a peak (cosine) or a rising midline crossing (sine) occurs."),
  N("Common traps", "- **Period is 2π ÷ B**, not B.\n- **Phase shift factor:** y = sin(2x − π) = sin(2(x − π/2)) shifts by **π/2**, not π. Factor B out first.\n- **Amplitude is a distance**, always positive.\n- **Tangent's period is π.**")
 ],
 "practice": [
  NUM("Amplitude of y = 5 sin x?", 5, "A = 5."),
  NUM("Amplitude of y = −3 cos x?", 3, "Size of A."),
  MC("Period of y = cos(x/2)?", ["π", "2π", "4π", "π/2"], 2, "2π ÷ (1/2) = 4π."),
  NUM("Midline of y = sin x − 4 (enter the y-value)?", -4, "D = −4."),
  NUM("Maximum value of y = 2 sin x + 3?", 5, "3 + 2."),
  MC("Period of y = tan x?", ["π", "2π", "π/2", "4π"], 0, "Tangent repeats every π."),
  NUM("Frequency of a wave with period 0.25 s?", 4, "1 ÷ 0.25.", unit="Hz"),
  MC("y = sin(x − π/3) is sin x shifted…", ["left π/3", "right π/3", "up π/3", "down π/3"], 1, "Phase shift right."),
  MC("Phase shift of y = cos(3x − π)?", ["π right", "π/3 right", "3π right", "π/3 left"], 1,
     "Factor: cos(3(x − π/3)). Shift **π/3 right**.",
     level="challenge", hint="Factor out B first."),
  MC("A wave has max 9 and min 1, with peaks every 8 seconds. Which model fits (cosine, peak at t = 0)?", ["y = 4 cos((π/4)t) + 5", "y = 8 cos(t) + 1", "y = 5 cos((π/4)t) + 4", "y = 4 cos(8t) + 5"], 0,
     "Midline (9 + 1)/2 = 5. Amplitude (9 − 1)/2 = 4. B = 2π/8 = π/4.",
     level="challenge", hint="Midline, amplitude, then B from the period."),
  NUM("Household current in some countries alternates at 50 Hz. How many milliseconds is one cycle?", 20,
      "Period = 1 ÷ 50 = 0.02 s = **20 ms**. (In the U.S., 60 Hz → about 16.7 ms.)",
      level="challenge", hint="Period = 1 ÷ frequency.", unit="ms"),
  NUM("Using h(t) = 2 cos((2π/365)(t − 172)) + 12, daylight hours at t = 172 + 182.5 (half a year later)?", 10,
      "The cosine argument becomes π: cos(π) = −1 → 2(−1) + 12 = **10 hours**.",
      level="challenge", hint="Half a period → cos goes from 1 to −1."),
 ],
 "sources": [PC, {"title": "OpenStax, Precalculus 2e, 6.1 Graphs of the Sine and Cosine Functions", "url": "https://openstax.org/books/precalculus-2e/pages/6-1-graphs-of-the-sine-and-cosine-functions"}]})

# ---------------------------------------------------------------- Trig identities
L.append({"id": "trig-identities", "title": "Trig identities", "band": "Grades 11–12", "minutes": 36,
 "lede": "Equations true for every angle. They let you rewrite trig expressions into simpler forms, solve trig equations, and prove why 45° is the best launch angle.",
 "sections": [
  T("## The six functions\n| Function | Definition |\n|---|---|\n| sin θ | y on the unit circle |\n| cos θ | x on the unit circle |\n| tan θ | sin θ ÷ cos θ |\n| csc θ (cosecant) | 1 ÷ sin θ |\n| sec θ (secant) | 1 ÷ cos θ |\n| cot θ (cotangent) | cos θ ÷ sin θ = 1 ÷ tan θ |"),
  T("## The core identities\n**Pythagorean** (from x² + y² = 1):\n- sin²θ + cos²θ = 1\n- 1 + tan²θ = sec²θ (divide the first by cos²θ)\n- 1 + cot²θ = csc²θ (divide by sin²θ)\n\n**Even/odd:**\n- cos(−θ) = cos θ (even: mirror across the x-axis keeps x)\n- sin(−θ) = −sin θ (odd)\n\n**Sum and difference:**\n- sin(A ± B) = sin A cos B ± cos A sin B\n- cos(A ± B) = cos A cos B ∓ sin A sin B (note the sign flip)\n\n**Double angle** (set A = B):\n- sin 2θ = 2 sin θ cos θ\n- cos 2θ = cos²θ − sin²θ = 1 − 2 sin²θ = 2 cos²θ − 1"),
  CHECK("Simplify 1 − sin²x.", ["cos x", "cos²x", "tan²x", "1"], 1, "From sin² + cos² = 1."),
  E("Exact value with a sum formula", "Find sin 75° exactly.",
    ["75° = 45° + 30°.", "sin(45° + 30°) = sin 45° cos 30° + cos 45° sin 30°", "= (√2/2)(√3/2) + (√2/2)(1/2)", "= (√6 + √2) ÷ 4"],
    "**(√6 + √2) ÷ 4 ≈ 0.966.** Check on a calculator: sin 75° ≈ 0.9659 ✓."),
  T("## Proving identities\nTo prove an identity, transform **one side** until it matches the other. Don't move terms across the equals sign; you're showing they're the same expression.\n\n**Strategies:**\n1. Start with the **more complicated** side.\n2. Rewrite everything in **sin and cos**.\n3. Look for **Pythagorean** substitutions.\n4. Combine fractions; factor.\n\n**Prove:** tan θ · cos θ = sin θ\n\ntan θ · cos θ = (sin θ ÷ cos θ) · cos θ = sin θ ✓"),
  T("## Solving trig equations\nUnlike identities, equations are true only for **certain** angles. Because trig functions repeat, there are usually **many** solutions; problems often ask for those in [0, 2π).\n\n**Solve 2 sin x − 1 = 0 on [0, 2π):**\n1. sin x = 1/2\n2. Reference angle π/6. Sine is positive in quadrants I and II.\n3. **x = π/6 or x = 5π/6**\n\n**Solve 2 cos²x − cos x − 1 = 0:** it's a quadratic in cos x: (2 cos x + 1)(cos x − 1) = 0 → cos x = −1/2 or cos x = 1 → x = 2π/3, 4π/3, or 0."),
  CHECK("Solutions to cos x = 0 on [0, 2π)?", ["0 and π", "π/2 and 3π/2", "π/4 and 3π/4", "only π/2"], 1, "Where the x-coordinate on the unit circle is 0."),
  E("Why 45° throws the farthest", "Ignoring air resistance, a projectile launched at speed v and angle θ on flat ground has range **R = v² sin(2θ) ÷ g**. Which angle maximizes R?",
    ["The double-angle identity created that sin(2θ): R = (2v² sin θ cos θ) ÷ g.", "sin(2θ) is largest (= 1) when 2θ = 90°.", "So θ = 45°."],
    "**45°.** And because sin(2θ) is symmetric around 45°, launches at 30° and 60° land at the **same** distance. Air resistance pushes the real-world optimum somewhat lower."),
  N("Common traps", "- **sin 2θ ≠ 2 sin θ.** Test: sin 60° ≈ 0.866, but 2 sin 30° = 1.\n- **sin(A + B) ≠ sin A + sin B.**\n- **Don't divide both sides by a trig function** when solving; you can lose solutions where it equals 0. Factor instead.\n- **Find every solution in the interval**, using the quadrant signs.")
 ],
 "practice": [
  MC("tan θ = ", ["cos θ / sin θ", "sin θ / cos θ", "1 / sin θ", "sin θ · cos θ"], 1, "Quotient identity."),
  MC("sec θ = ", ["1 / sin θ", "1 / cos θ", "1 / tan θ", "cos θ / sin θ"], 1, "Reciprocal of cosine."),
  MC("1 + tan²θ = ", ["sec²θ", "csc²θ", "cos²θ", "1"], 0, "Pythagorean."),
  MC("sin(−θ) = ", ["sin θ", "−sin θ", "cos θ", "−cos θ"], 1, "Odd."),
  MC("sin 2θ = ", ["2 sin θ", "2 sin θ cos θ", "sin²θ − cos²θ", "sin θ + cos θ"], 1, "Double angle."),
  MC("Simplify sin x · csc x.", ["0", "1", "sin²x", "cos x"], 1, "csc x = 1/sin x."),
  MC("Solutions of sin x = 1 on [0, 2π)?", ["0", "π/2", "π", "π/2 and 3π/2"], 1, "Top of the circle only."),
  MC("Simplify (sin²x + cos²x) ÷ cos x.", ["tan x", "sec x", "1", "sin x"], 1, "1 ÷ cos x."),
  MC("Solve sin x = −√3/2 on [0, 2π).", ["π/3, 2π/3", "4π/3, 5π/3", "7π/6, 11π/6", "5π/6, 7π/6"], 1,
     "Reference angle π/3. Sine negative in III and IV: π + π/3 = 4π/3 and 2π − π/3 = 5π/3.",
     level="challenge", hint="Reference angle, then the quadrants where sine is negative."),
  NUM("cos 15° exactly is (√6 + √2)/4. To 4 decimals?", 0.9659,
      "Using cos(45° − 30°) = cos45 cos30 + sin45 sin30 = (√6 + √2)/4 ≈ **0.9659**. (Same as sin 75°, because they're complementary.)",
      level="challenge", hint="Compute (2.4495 + 1.4142) ÷ 4.", tol=0.0002),
  MC("If sin θ = 3/5 and cos θ = 4/5, then sin 2θ = ?", ["6/5", "24/25", "7/25", "12/25"], 1,
     "2 · (3/5)(4/5) = **24/25**.",
     level="challenge", hint="sin 2θ = 2 sin θ cos θ."),
  NUM("A ball is launched at 20 m/s at 30° on flat ground. Range R = v² sin(2θ)/g (g = 9.8)? (1 decimal)", 35.3,
      "sin 60° ≈ 0.8660. R = 400 × 0.8660 ÷ 9.8 ≈ **35.3 m**. At 60° it would land in the same spot.",
      level="challenge", hint="2θ = 60°.", tol=0.06, unit="m"),
 ],
 "sources": [PC, {"title": "OpenStax, Precalculus 2e, 7.1 Solving Trigonometric Equations with Identities", "url": "https://openstax.org/books/precalculus-2e/pages/7-1-solving-trigonometric-equations-with-identities"}]})

# ---------------------------------------------------------------- Vectors
L.append({"id": "vectors", "title": "Vectors", "band": "Grades 11–12", "minutes": 34,
 "lede": "Quantities with both size and direction: forces, velocities, wind. Break them into components, add them, and find the result. How pilots fly through crosswinds and how two tow straps share a load.",
 "sections": [
  T("## Scalars vs vectors\n- **Scalar**: size only. Speed (60 mph), mass, temperature, time.\n- **Vector**: size **and** direction. Velocity (60 mph north), force, displacement, acceleration.\n\nA vector is drawn as an arrow: its **length** is its **magnitude**, and it points in its **direction**. Written as **v** (bold) or with an arrow over it."),
  T("## Components\nAny 2D vector can be split into horizontal and vertical **components**:\n\n**vₓ = |v| cos θ** and **v_y = |v| sin θ** (θ measured from the positive x-axis)\n\nGoing back:\n\n**|v| = √(vₓ² + v_y²)** and **θ = tan⁻¹(v_y ÷ vₓ)** (then check the quadrant)\n\n*A force of 100 N at 30°:* Fₓ = 100 cos 30° ≈ 86.6 N, F_y = 100 sin 30° = 50 N."),
  CHECK("A vector has components (6, 8). Its magnitude is…", ["14", "10", "48", "2"], 1, "√(36 + 64) = 10."),
  T("## Adding vectors\n**Graphically:** place them **tip to tail**; the sum (the **resultant**) runs from the start of the first to the tip of the last.\n\n**With components (the reliable way):** add the x's and add the y's.\n\n(3, 4) + (5, −1) = **(8, 3)**\n\n**Scalar multiplication** stretches a vector: 2(3, 4) = (6, 8), twice as long, same direction. A negative scalar flips it."),
  E("Two tow straps", "Two straps pull a stuck truck: 3,000 N due east and 4,000 N due north. What's the total force?",
    ["Components: (3,000, 0) + (0, 4,000) = (3,000, 4,000).", "Magnitude: √(3,000² + 4,000²) = 5,000 N.", "Direction: tan⁻¹(4,000/3,000) ≈ 53.1° north of east."],
    "**5,000 N at about 53° north of east.** Two straps at right angles give less total pull than 7,000 N in a straight line. Angled forces partly work against each other's usefulness."),
  T("## Velocity with wind or current\nWhen a plane flies through wind, or a boat crosses a river, its **actual** velocity is the **vector sum** of its own velocity and the wind or current.\n\n*A plane heads due north at 200 km/h with a 50 km/h wind blowing due east.* Ground velocity = (50, 200). Speed = √(2,500 + 40,000) ≈ **206 km/h**, drifting about tan⁻¹(50/200) ≈ **14° east of north**. To actually go north, the pilot must point the nose partly **into** the wind.\n\nCrosswinds push on tall, flat trailers the same way, which is why high-profile vehicles get wind warnings on bridges."),
  CHECK("(2, −3) + (−5, 7) = ?", ["(−3, 4)", "(7, −10)", "(−3, −10)", "(3, 4)"], 0, "2 − 5 = −3; −3 + 7 = 4."),
  T("## The dot product\n**a · b = aₓbₓ + a_yb_y** = |a||b| cos θ\n\nIt measures how much two vectors point the **same way**:\n- positive: less than 90° apart\n- **zero**: **perpendicular**\n- negative: more than 90° apart\n\nIn physics, **work = F · d**: only the part of the force along the motion does work. That's the cos θ from the work-and-energy lesson."),
  N("Common traps", "- **Magnitudes don't simply add** unless vectors point the same way. 3 + 4 can be 5.\n- **Check the quadrant** after tan⁻¹: (−3, −4) points into quadrant III, not I.\n- **Angles from the x-axis** for the cos/sin component formulas. Bearings (from north) need adjusting.\n- **Dot product gives a scalar**, not a vector.")
 ],
 "practice": [
  MC("Which is a vector?", ["speed of 50 mph", "mass of 80 kg", "velocity of 50 mph west", "temperature of 30 °C"], 2, "Has direction."),
  NUM("Magnitude of (5, 12)?", 13, "√(25 + 144)."),
  MC("(4, 1) + (−1, 6) = ?", ["(3, 7)", "(5, 7)", "(3, −5)", "(−4, 6)"], 0, "Add components."),
  MC("3(2, −1) = ?", ["(6, −3)", "(5, 2)", "(6, 3)", "(2, −3)"], 0, "Multiply each component."),
  NUM("x-component of a 10 N force at 60°? (cos 60° = 0.5)", 5, "10 × 0.5.", unit="N"),
  NUM("Dot product of (2, 3) and (4, −1)?", 5, "8 − 3."),
  MC("If a · b = 0 (both nonzero), the vectors are…", ["parallel", "perpendicular", "equal", "opposite"], 1, "cos 90° = 0."),
  NUM("Two perpendicular forces of 6 N and 8 N. Resultant magnitude?", 10, "√(36 + 64).", unit="N"),
  NUM("A boat heads straight across a river at 4 m/s; the current flows at 3 m/s downstream. Actual speed?", 5,
      "√(16 + 9) = **5 m/s**, angled downstream.",
      level="challenge", hint="Perpendicular components.", unit="m/s"),
  NUM("Direction of the vector (−3, 3), in degrees from the positive x-axis?", 135,
      "tan⁻¹(3/−3) gives −45° on a calculator, but the vector points into **quadrant II**: 180° − 45° = **135°**.",
      level="challenge", hint="Calculators don't know the quadrant.", unit="°"),
  NUM("A 500 N pull at 30° above horizontal drags a sled 10 m along flat ground. Work done? (cos 30° ≈ 0.866)", 4330,
      "W = F d cos θ = 500 × 10 × 0.866 = **4,330 J**. The upward part of the pull does no work.",
      level="challenge", hint="Only the horizontal component counts.", tol=1, unit="J"),
  MC("A plane must reach a city due north, with wind blowing from west to east. The pilot should point the nose…", ["due north", "slightly east of north", "slightly west of north", "due west"], 2,
     "Aim partly **into** the wind so the eastward drift cancels and the resultant points north.",
     level="challenge", hint="Cancel the wind's component."),
 ],
 "sources": [PC, {"title": "OpenStax, Precalculus 2e, 8.8 Vectors", "url": "https://openstax.org/books/precalculus-2e/pages/8-8-vectors"}]})

# ---------------------------------------------------------------- Introduction to limits
L.append({"id": "introduction-to-limits", "title": "Introduction to limits", "band": "Grades 11–12", "minutes": 36,
 "lede": "The idea calculus is built on: what value does a function approach as the input gets closer and closer to some number? The answer lets us talk about speed at a single instant.",
 "sections": [
  T("## The question limits answer\nYour average speed over a trip is distance ÷ time. But what's your speed **at exactly 2:15 p.m.**? Over zero time you travel zero distance: 0 ÷ 0. Meaningless.\n\nThe trick: compute the average over **shorter and shorter** intervals and see what number those averages **approach**. That number is a **limit**, and the instant speed it gives is what your speedometer shows. Isaac Newton and Gottfried Leibniz built calculus on this idea in the late 1600s."),
  T("## Notation and meaning\n**lim (x→a) f(x) = L**\n\nmeans: as x gets **arbitrarily close** to a (from both sides, but **not equal** to a), f(x) gets arbitrarily close to L.\n\nThe value **at** a doesn't matter. f(a) might be different, or undefined, and the limit can still exist."),
  E("Estimate a limit with a table", "Estimate lim (x→3) of (x² − 9) ÷ (x − 3).",
    ["At x = 3: 0 ÷ 0, undefined. So look nearby:", "x = 2.9 → 5.9 · x = 2.99 → 5.99 · x = 2.999 → 5.999", "x = 3.1 → 6.1 · x = 3.01 → 6.01 · x = 3.001 → 6.001"],
    "The outputs close in on **6** from both sides. The limit is 6, even though the function is undefined at 3."),
  T("## Computing limits\n**1. Direct substitution.** If f is continuous at a (polynomials, most familiar functions where they're defined), just plug in: lim (x→2) of (x² + 1) = **5**.\n\n**2. If you get 0/0, simplify first.** It's an *indeterminate form*: a signal to do algebra, not an answer.\n\n(x² − 9) ÷ (x − 3) = (x + 3)(x − 3) ÷ (x − 3) = x + 3 (for x ≠ 3) → plug in: **6**. Matches the table.\n\n**3. If you get (nonzero) ÷ 0**, the function blows up: the limit doesn't exist as a finite number (there's a vertical asymptote)."),
  CHECK("lim (x→4) of (x² − 16) ÷ (x − 4) = ?", ["0", "4", "8", "doesn't exist"], 2, "Factor: x + 4 → 8."),
  T("## One-sided limits\nSometimes a function approaches **different** values from the left and right.\n\n- **lim (x→a⁻)**: from the **left** (values less than a)\n- **lim (x→a⁺)**: from the **right**\n\nThe (two-sided) limit exists **only if both one-sided limits exist and are equal**.\n\n*A shipping rate that's $100 up to 500 lb and $150 above:* approaching 500 lb from below gives 100; from above, 150. The two-sided limit at 500 lb **doesn't exist**: there's a **jump**."),
  T("## Limits at infinity\n**lim (x→∞) f(x)** asks what happens as x grows without bound: the **end behavior**, and the horizontal asymptote from the rational functions lesson.\n\n- lim (x→∞) 1/x = **0**\n- lim (x→∞) (3x² + 1) ÷ (x² − 5) = **3** (leading coefficients, same degree)\n- lim (x→∞) of the average cost C(x) = (6,000 + 0.9x) ÷ x = **0.9**: your cost per mile approaches the variable cost as miles grow."),
  T("## Continuity\nA function is **continuous at a** if you can draw through that point without lifting your pencil. Formally, three things must hold:\n\n1. f(a) is defined,\n2. lim (x→a) f(x) exists, and\n3. they're **equal**.\n\nThree ways to fail: a **hole** (removable), a **jump**, or an **infinite** (asymptote) discontinuity."),
  CHECK("f(x) = (x² − 1)/(x − 1) at x = 1 has…", ["a jump", "a removable discontinuity (hole)", "an asymptote", "no discontinuity"], 1, "Simplifies to x + 1, limit 2, but f(1) is undefined: a hole."),
  N("Common traps", "- **0/0 isn't the answer.** It means *simplify*.\n- **The limit ignores f(a) itself.**\n- **Both sides must agree** for the limit to exist.\n- **∞ isn't a number.** A limit that \"equals ∞\" technically doesn't exist; it describes unbounded growth.")
 ],
 "practice": [
  NUM("lim (x→3) of (2x + 1)?", 7, "Direct substitution."),
  NUM("lim (x→−1) of (x² + 4x)?", -3, "1 − 4 = −3."),
  NUM("lim (x→5) of (x² − 25) ÷ (x − 5)?", 10, "Factor → x + 5 → 10."),
  NUM("lim (x→∞) of 7 ÷ x?", 0, "Shrinks to 0."),
  NUM("lim (x→∞) of (4x + 1) ÷ (2x − 3)?", 2, "Leading coefficients: 4/2."),
  MC("If the left-hand limit is 3 and the right-hand limit is 5, the two-sided limit…", ["is 4", "is 3", "doesn't exist", "is 5"], 2, "Must agree."),
  MC("0/0 from direct substitution means…", ["the limit is 0", "the limit doesn't exist", "simplify and try again", "the limit is 1"], 2, "Indeterminate form."),
  MC("A function with a jump at x = 2 is…", ["continuous at 2", "discontinuous at 2", "undefined everywhere", "linear"], 1, "Lifting the pencil."),
  NUM("lim (x→2) of (x² + x − 6) ÷ (x − 2)?", 5,
      "Factor: (x + 3)(x − 2) ÷ (x − 2) = x + 3 → **5**.",
      level="challenge", hint="Factor the top."),
  NUM("lim (h→0) of ((3 + h)² − 9) ÷ h?", 6,
      "Expand: (9 + 6h + h² − 9) ÷ h = (6h + h²) ÷ h = 6 + h → **6**. (This is the slope of x² at x = 3: your first derivative.)",
      level="challenge", hint="Expand, cancel h, then let h → 0."),
  NUM("Average speed from t = 2 to t = 2 + h for position s(t) = t² (meters, seconds): (s(2 + h) − s(2)) ÷ h. As h → 0, what's the instantaneous speed?", 4,
      "((2 + h)² − 4) ÷ h = (4h + h²) ÷ h = 4 + h → **4 m/s**.",
      level="challenge", hint="Same algebra as the last problem.", unit="m/s"),
  NUM("Estimate lim (x→0) of sin(x) ÷ x (x in radians) using x = 0.01: sin(0.01) ≈ 0.0099998. (3 decimals)", 1,
      "0.0099998 ÷ 0.01 ≈ 0.99998 → the limit is **1**. A famous limit, and one reason radians are the natural unit.",
      level="challenge", hint="Divide.", tol=0.001),
 ],
 "sources": [C1, {"title": "OpenStax, Calculus Volume 1, 2.2 The Limit of a Function", "url": "https://openstax.org/books/calculus-volume-1/pages/2-2-the-limit-of-a-function"}]})

save("math", L)
