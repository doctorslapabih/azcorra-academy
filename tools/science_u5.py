from common import *

AST = {"title": "OpenStax, Astronomy 2e", "url": "https://openstax.org/details/books/astronomy-2e"}
USGS = {"title": "USGS, This Dynamic Earth: The Story of Plate Tectonics", "url": "https://pubs.usgs.gov/publication/7000097"}
JET = {"title": "NOAA / National Weather Service, JetStream: An Online School for Weather", "url": "https://www.noaa.gov/jetstream"}
CLIM = {"title": "NOAA Climate.gov", "url": "https://www.climate.gov/"}
NASA = {"title": "NASA Science: Solar System", "url": "https://science.nasa.gov/solar-system/"}
L = []


def FIG(svg, caption): return {"type": "figure", "svg": svg, "caption": caption}


LAYERS = """<svg viewBox="0 0 420 230" width="100%" style="max-width:520px" role="img" aria-label="Earth's layers">
<g font-family="inherit" font-size="13" fill="currentColor">
<path d="M20 210 A190 190 0 0 1 210 20 L210 210 Z" fill="currentColor" fill-opacity=".10"/>
<path d="M40 210 A170 170 0 0 1 210 40 L210 210 Z" fill="currentColor" fill-opacity=".18"/>
<path d="M110 210 A100 100 0 0 1 210 110 L210 210 Z" fill="currentColor" fill-opacity=".30"/>
<path d="M160 210 A50 50 0 0 1 210 160 L210 210 Z" fill="currentColor" fill-opacity=".50"/>
<line x1="20" y1="210" x2="210" y2="210" stroke="currentColor" stroke-opacity=".4"/>
<text x="232" y="34">Crust · 5–70 km thick</text>
<text x="232" y="82">Mantle · hot rock that slowly flows</text>
<text x="232" y="98" fill-opacity=".7">down to ~2,900 km</text>
<text x="232" y="146">Outer core · liquid iron and nickel</text>
<text x="232" y="194">Inner core · solid, ~5,000 °C+</text>
<line x1="200" y1="28" x2="228" y2="30" stroke="currentColor" stroke-opacity=".5"/>
<line x1="180" y1="80" x2="228" y2="80" stroke="currentColor" stroke-opacity=".5"/>
<line x1="175" y1="140" x2="228" y2="142" stroke="currentColor" stroke-opacity=".5"/>
<line x1="198" y1="190" x2="228" y2="190" stroke="currentColor" stroke-opacity=".5"/>
</g></svg>"""

# ---------------------------------------------------------------- Plate tectonics
L.append({"id": "plate-tectonics", "title": "Plate tectonics", "band": "Grades 7–8", "minutes": 32,
 "lede": "The ground under you is moving right now, about as fast as your fingernails grow. That slow motion builds mountains, opens oceans, and causes nearly every earthquake and volcano on Earth.",
 "sections": [
  T("## Inside the Earth\nEarth is layered like a peach: a thin skin, a thick middle and a dense pit.\n\n| Layer | What it's like |\n|---|---|\n| **Crust** | thin, solid rock. Thinnest under the oceans (~5–10 km), thickest under mountains (up to ~70 km) |\n| **Mantle** | solid but extremely hot rock that **flows very slowly** over millions of years, like super-thick putty. About 2,900 km thick |\n| **Outer core** | **liquid** iron and nickel. Its swirling creates Earth's magnetic field |\n| **Inner core** | **solid** iron and nickel, as hot as the Sun's surface, kept solid by enormous pressure |\n\nThe **lithosphere** (the crust plus the stiff top of the mantle) is broken into about a dozen large **tectonic plates**, which ride on the softer, flowing layer beneath."),
  FIG(LAYERS, "A slice of the Earth (not to scale). The whole crust is thinner, relative to Earth, than the skin of an apple."),
  T("## How we figured it out\n- **1912:** German scientist **Alfred Wegener** proposed **continental drift**. The continents fit like puzzle pieces (look at South America and Africa), matching fossils and rock layers appear on continents now separated by oceans, and glacier scratches show up in places that are now tropical. He was largely **rejected**: he couldn't explain **what** moved the continents.\n- **1950s–60s:** mapping the ocean floor revealed a huge underwater mountain chain, the **Mid-Atlantic Ridge**, where new seafloor forms and spreads outward (**seafloor spreading**). Magnetic stripes in the rock, recording reversals of Earth's magnetic field, matched perfectly on both sides of the ridge.\n- Together, these became the theory of **plate tectonics**. Wegener was right about the drifting; the mechanism was the part he was missing.\n\n**What drives it:** heat from Earth's interior keeps the mantle slowly churning, and cold, dense plate edges sink back into the mantle, **pulling** the rest of the plate along behind them."),
  T("## The three types of boundaries\n| Boundary | Plates… | Creates | Real example |\n|---|---|---|---|\n| **Divergent** | move **apart** | new crust, rift valleys, mid-ocean ridges | Mid-Atlantic Ridge; East African Rift; Iceland |\n| **Convergent** | move **together** | mountains, deep trenches, volcanoes, big earthquakes | Himalayas; Andes; Japan |\n| **Transform** | **slide past** each other | earthquakes (no new or destroyed crust) | San Andreas Fault, California |\n\n**Convergent boundaries come in three kinds:**\n- **Ocean meets continent:** the denser ocean plate **subducts** (dives under), melts, and feeds a chain of volcanoes. *The Andes.*\n- **Ocean meets ocean:** one subducts, forming a deep trench and volcanic islands. *Japan; the Mariana Trench, the deepest place on Earth.*\n- **Continent meets continent:** neither sinks easily, so the crust crumples upward. *India crashing into Asia built the Himalayas, which are still rising.*"),
  CHECK("Plates sliding horizontally past each other form a…", ["divergent boundary", "convergent boundary", "transform boundary", "subduction zone"], 2, "Like the San Andreas Fault. Crust is neither created nor destroyed, but stress builds and releases as earthquakes."),
  T("## Earthquakes and volcanoes\nPlates don't slide smoothly. They **lock**, stress builds for years or centuries, and then the rock snaps. The energy released travels as **seismic waves**: that's an earthquake.\n\n**Magnitude** measures the energy released. The scale is **logarithmic**:\n- each whole step up means about **10×** bigger ground shaking (wave amplitude), and\n- about **32×** more **energy**.\n\nSo a magnitude 7 releases roughly 32 × 32 ≈ **1,000 times** the energy of a magnitude 5.\n\nMost volcanoes and earthquakes sit along plate boundaries. The **Ring of Fire** around the Pacific Ocean, a loop of subduction zones, holds most of the world's active volcanoes and has most of its large earthquakes. **Florida**, in the middle of the North American Plate, far from any boundary, has very few."),
  E("How far is far?", "The Atlantic Ocean widens about **2.5 cm per year**. How much wider will it be in 1 million years?",
    ["2.5 cm × 1,000,000 = 2,500,000 cm.", "2,500,000 cm = 25,000 m = **25 km**."],
    "**About 25 km.** Slow for a lifetime, huge for geology. Over ~200 million years, that kind of spreading opened the entire Atlantic, splitting the supercontinent **Pangaea**."),
  CHECK("Why does the ocean plate sink when it meets a continent?", ["It's lighter", "It's denser", "It's hotter", "It's moving faster"], 1, "Ocean crust is made of denser rock (basalt) than continental crust (granite-like rock), so it dives under."),
  N("Common traps", "- **The mantle isn't a sea of lava.** It's almost entirely solid rock that flows extremely slowly. Magma forms in specific places, like above subduction zones.\n- **Continents don't float on the ocean.** Plates include both ocean floor and continents, moving together.\n- **Magnitude 8 isn't twice magnitude 4.** It's about 10,000× the shaking amplitude and about a million times the energy.")
 ],
 "practice": [
  MC("Which layer is **liquid**?", ["crust", "mantle", "outer core", "inner core"], 2, "Liquid iron and nickel. Its motion creates the magnetic field."),
  MC("Who first proposed continental drift?", ["Charles Darwin", "Alfred Wegener", "Isaac Newton", "Harry Hess"], 1, "In 1912. Rejected for decades because he lacked a mechanism."),
  MC("New crust forms at…", ["divergent boundaries", "convergent boundaries", "transform boundaries", "the inner core"], 0, "Plates pull apart and magma rises to fill the gap."),
  MC("The Himalayas formed from…", ["a divergent boundary", "two continental plates colliding", "a transform fault", "a hot spot"], 1, "India pushing into Asia."),
  MC("The San Andreas Fault is a ___ boundary.", ["divergent", "convergent", "transform", "subduction"], 2, "Plates sliding past each other."),
  NUM("A plate moves 5 cm per year. How many **kilometers** does it move in 1 million years?", 50, "5 × 1,000,000 = 5,000,000 cm = 50,000 m = 50 km.", unit="km"),
  MC("When an ocean plate dives under another plate, it's called…", ["spreading", "subduction", "erosion", "drift"], 1, "From Latin *sub* (under) + *ducere* (to lead)."),
  MC("Why does Florida have few earthquakes?", ["It's too flat", "It's far from any plate boundary", "Water absorbs them", "It's on the Pacific Plate"], 1, "It sits in the middle of the North American Plate."),
  NUM("About how many times more **energy** does a magnitude 6 earthquake release than a magnitude 4?", 1000,
      "Two steps up: 32 × 32 ≈ **1,000**. (The shaking amplitude is 10 × 10 = 100× bigger.)",
      level="challenge", hint="Each step is about 32× the energy.", tol=50,
      steps=["Magnitude 4 → 5: ×32.", "Magnitude 5 → 6: ×32 again.", "32 × 32 = 1,024 ≈ 1,000."]),
  MC("Magnetic stripes in the seafloor were key evidence because…", ["they prove the Moon pulls the plates", "matching patterns on both sides of the ridge show new crust forming and spreading outward", "they show where gold is", "they show the core is solid"], 1,
     "Rock records Earth's magnetic direction as it cools. Mirror-image stripes on both sides mean the seafloor is growing from the middle.",
     level="challenge", hint="Why would the patterns be mirror images?"),
  MC("Mount Fuji and the deep trenches near Japan are best explained by…", ["continent-continent collision", "ocean-ocean (and ocean-continent) subduction", "a divergent boundary", "a transform fault"], 1,
     "Subducting ocean plates create trenches and melt to feed volcanoes.",
     level="challenge", hint="Trench + volcanoes = one plate diving under another."),
  MC("Wegener's evidence was strong but his idea was rejected. What was the main problem?", ["His fossils were fake", "He couldn't explain what force moved the continents", "Continents don't fit together", "He was from Germany"], 1,
     "Good science needs a **mechanism**, not just a pattern. Mantle convection and seafloor spreading supplied it in the 1960s. A lesson in why *how* matters as much as *what*.",
     level="challenge", hint="Pattern without explanation."),
 ],
 "sources": [USGS, {"title": "USGS, Earthquake Magnitude, Energy Release, and Shaking Intensity", "url": "https://www.usgs.gov/programs/earthquake-hazards/earthquake-magnitude-energy-release-and-shaking-intensity"}]})

# ---------------------------------------------------------------- Weather and climate
L.append({"id": "weather-and-climate", "title": "Weather and climate", "band": "Grades 7–8", "minutes": 34,
 "lede": "Why air moves, how storms form, what makes a hurricane, and the difference between today's forecast and a 30-year trend. Useful science for anyone who drives for a living or lives in Florida.",
 "sections": [
  T("## Weather vs climate\n- **Weather** is the condition of the atmosphere **right now** or over a few days: temperature, rain, wind, humidity.\n- **Climate** is the **long-term average** pattern for a place, usually measured over **30 years**.\n\nA saying that captures it: *climate is what you expect, weather is what you get.* One cold week doesn't change a climate, just like one bad trade doesn't define a strategy. Both are about the **average over many samples**."),
  T("## The engine: uneven heating\nThe Sun heats Earth **unevenly**: the equator gets direct rays, the poles get slanted ones. Land heats faster than water. That uneven heating drives everything:\n\n1. Warm air is **less dense**, so it **rises**. That leaves **low pressure** below.\n2. Cool air is **denser** and **sinks**, creating **high pressure**.\n3. Air flows from **high pressure to low pressure**. That flow is **wind**.\n\n| | High pressure | Low pressure |\n|---|---|---|\n| Air is | sinking | rising |\n| Usually brings | clear, calm, dry weather | clouds, rain, storms |\n| Why | sinking air warms and dries out | rising air cools, and its water vapor condenses into clouds |\n\nThe **troposphere** (the lowest layer of the atmosphere, roughly the bottom 8–18 km) is where almost all weather happens. In it, temperature drops about **6.5 °C per kilometer** you climb. That's why mountain passes can be icy when the valley is just wet."),
  CHECK("Why does rising air tend to form clouds?", ["It gets warmer", "It cools, and water vapor condenses", "It picks up dust", "It speeds up"], 1, "Cooler air can hold less water vapor. The excess condenses into droplets: clouds."),
  T("## Fronts: where air masses collide\nAn **air mass** is a huge body of air with similar temperature and humidity. The boundary between two is a **front**.\n\n| Front | What happens | Weather |\n|---|---|---|\n| **Cold front** | cold air **shoves under** warm air, forcing it up fast | quick, intense storms, then cooler, drier, clear air |\n| **Warm front** | warm air **slides up over** cold air gradually | long periods of light rain or drizzle, then warmer |\n| **Stationary front** | neither side moves | days of clouds and rain in the same place |\n\nThe **water cycle** ties it together: water **evaporates**, **condenses** into clouds, falls as **precipitation**, and collects as **runoff** and groundwater, then evaporates again."),
  T("## Severe weather\n**Thunderstorms** form when warm, moist air rises fast. Lightning heats the air to roughly five times the temperature of the Sun's surface, and the air explodes outward: thunder.\n\n**Flash-to-bang rule:** sound travels about **1 mile every 5 seconds**. Count seconds between the lightning and the thunder, divide by 5, and you get the distance in miles. *If you can hear thunder, you're close enough to be struck.*\n\n**Hurricanes** form over **warm ocean water** (at least about 26–27 °C, or 80 °F). Warm, moist air rises, pulls in more air below, and Earth's rotation sets it spinning: **counterclockwise** in the Northern Hemisphere. They weaken over land or cold water because they lose their fuel.\n\n| Saffir–Simpson category | Sustained winds |\n|---|---|\n| 1 | 74–95 mph |\n| 2 | 96–110 mph |\n| 3 (major) | 111–129 mph |\n| 4 | 130–156 mph |\n| 5 | 157 mph or higher |\n\nIn a hurricane, **storm surge** and **flooding** usually cause more deaths than the wind. *Turn around, don't drown*: about a foot of moving water can float many vehicles."),
  E("Flash to bang", "You see lightning while fueling, and hear thunder 15 seconds later. How far away is the strike?", ["15 ÷ 5 = 3."], "**About 3 miles.** Well within striking range. Lightning can hit 10 miles or more from the storm. Get in the cab."),
  T("## What sets a place's climate\n1. **Latitude**: closer to the equator = more direct sunlight = warmer.\n2. **Altitude**: higher = colder (that 6.5 °C per km).\n3. **Nearness to water**: oceans heat and cool slowly, so coastal places have milder swings than inland ones.\n4. **Ocean currents**: the **Gulf Stream** carries warm water from the Gulf of Mexico up the U.S. East Coast and across to Europe, helping keep western Europe milder than its latitude suggests.\n5. **Mountains**: the side facing incoming wind gets rain; the far side sits in a dry **rain shadow**."),
  T("## The greenhouse effect and climate change\nSunlight passes through the atmosphere and warms the ground. The ground gives off heat (infrared). **Greenhouse gases**, mainly water vapor, **carbon dioxide (CO₂)** and **methane**, absorb some of that heat and send part of it back down. Without this natural effect, Earth would average about −18 °C (0 °F) and be frozen.\n\nBurning coal, oil and gas releases CO₂. Atmospheric CO₂ has risen from about **280 parts per million** before the Industrial Revolution to **more than 420 ppm** today, and global average temperature has risen **more than 1 °C** since the late 1800s. That's the **enhanced** greenhouse effect, and it's what scientists mean by climate change."),
  CHECK("A record cold week in Ohio. Does this disprove global warming?", ["Yes", "No: one week of weather isn't a climate trend", "Only if it snows", "Yes, if it happens in summer"], 1, "Climate is the long-term **average** across the whole planet. One local week is a single data point."),
  N("Common traps", "- **Seasons aren't caused by distance from the Sun**, and **weather isn't climate**. (Seasons are next lesson.)\n- **Hurricane category measures wind only.** A Category 1 can still cause deadly flooding.\n- **The greenhouse effect itself isn't bad.** It keeps Earth livable. The issue is **strengthening** it.\n- **Humid air is actually less dense** than dry air at the same temperature (water vapor is lighter than nitrogen and oxygen), one reason moist air rises into storms.")
 ],
 "practice": [
  MC("Climate is usually defined as the average weather over about…", ["1 year", "5 years", "30 years", "1,000 years"], 2, "The standard climate period."),
  MC("Wind blows from…", ["low to high pressure", "high to low pressure", "cold to hot only", "west to east only"], 1, "Air moves from high pressure toward low."),
  MC("High pressure usually brings…", ["storms", "clear, calm weather", "hurricanes", "tornadoes"], 1, "Sinking air warms and dries."),
  MC("A cold front typically brings…", ["days of drizzle", "fast, intense storms then clearing", "no change", "fog only"], 1, "Warm air is shoved up fast."),
  NUM("Thunder comes 20 seconds after lightning. About how many miles away is it?", 4, "20 ÷ 5 = 4.", unit="miles"),
  MC("Hurricanes need…", ["cold water", "warm ocean water", "mountains", "dry air"], 1, "Warm water is the fuel."),
  MC("In the Northern Hemisphere, hurricanes spin…", ["clockwise", "counterclockwise", "either way at random", "they don't spin"], 1, "Due to Earth's rotation (the Coriolis effect)."),
  MC("Why are coastal cities usually milder than inland cities at the same latitude?", ["Sea breezes are always cold", "Water heats and cools slowly, evening out temperatures", "There's less sunlight on the coast", "Salt warms the air"], 1, "Oceans act as a heat buffer."),
  NUM("It's 10 °C at a valley truck stop. You climb a pass 2 km higher. Using 6.5 °C per km, what's the temperature at the top?", -3,
      "Drop: 2 × 6.5 = 13 °C. 10 − 13 = **−3 °C**. Wet roads in the valley can be **ice** at the summit.",
      level="challenge", hint="Multiply the climb by the cooling rate, then subtract.", unit="°C"),
  MC("A hurricane has 125 mph sustained winds. Its category is…", ["1", "2", "3", "4"], 2,
     "111–129 mph = **Category 3**, the first \"major\" hurricane category.",
     level="challenge", hint="Use the Saffir–Simpson table."),
  MC("A city on the windward side of a mountain range gets 80 inches of rain a year. A city on the other side gets 10. Why?", ["The second city is higher", "Air rises and drops its moisture on the windward side, leaving a dry rain shadow", "The second city is closer to the equator", "Mountains block sunlight"], 1,
     "Rising air cools and rains out. By the time it crosses and sinks, it's dry.",
     level="challenge", hint="What happens to air forced up a mountain?"),
  MC("Without any greenhouse effect, Earth's average temperature would be about…", ["15 °C, the same", "−18 °C, frozen", "100 °C, boiling", "40 °C, tropical"], 1,
     "The natural greenhouse effect warms Earth by about 33 °C, from −18 °C to about 15 °C. The problem is adding to it, not having it.",
     level="challenge", hint="The greenhouse effect is what keeps us warm."),
 ],
 "sources": [JET, CLIM, {"title": "NOAA National Hurricane Center: Saffir-Simpson Hurricane Wind Scale", "url": "https://www.nhc.noaa.gov/aboutsshws.php"}, {"title": "NOAA / NWS: Lightning Safety", "url": "https://www.weather.gov/safety/lightning"}]})

# ---------------------------------------------------------------- The solar system
L.append({"id": "the-solar-system", "title": "The solar system", "band": "Grades 7–8", "minutes": 32,
 "lede": "Eight planets, a star holding 99.8% of all the mass, and the real reason we have seasons (most adults get it wrong).",
 "sections": [
  T("## The Sun runs the show\nThe solar system formed about **4.6 billion years ago** from a collapsing cloud of gas and dust. Most of the material fell to the center and became the **Sun**, which holds about **99.8%** of the solar system's mass. Its gravity holds everything else in orbit.\n\nDistances here are so big we use a special unit: the **astronomical unit (AU)**, Earth's average distance from the Sun, about **150 million km** (93 million miles). Light covers that in about **8 minutes and 20 seconds**. When you see the Sun, you're seeing it as it was 8 minutes ago."),
  T("## The planets\n**Memory trick:** *My Very Educated Mother Just Served Us Nachos.*\n\n| Planet | Type | Distance (AU) | One fact worth remembering |\n|---|---|---|---|\n| Mercury | rocky | 0.39 | smallest; no real atmosphere, so huge day/night swings |\n| Venus | rocky | 0.72 | **hottest** planet (~465 °C): runaway greenhouse effect |\n| Earth | rocky | 1.00 | only known world with liquid surface oceans and life |\n| Mars | rocky | 1.52 | red from iron oxide (rust); tallest volcano, Olympus Mons |\n| Jupiter | gas giant | 5.2 | largest; the Great Red Spot is a storm bigger than Earth |\n| Saturn | gas giant | 9.5 | brightest rings, made of ice and rock chunks |\n| Uranus | ice giant | 19.2 | tipped on its side, rolls around the Sun |\n| Neptune | ice giant | 30.1 | fastest winds in the solar system |\n\n**Inner planets** are small and rocky. **Outer planets** are giants made mostly of gas and ices. Between Mars and Jupiter is the **asteroid belt**. Beyond Neptune is the **Kuiper Belt**, home of icy bodies including **Pluto**."),
  CHECK("Mercury is closest to the Sun, but Venus is hotter. Why?", ["Venus is bigger", "Venus's thick CO₂ atmosphere traps heat", "Venus spins faster", "Mercury is made of ice"], 1, "A runaway greenhouse effect. Venus is hot enough to melt lead, day and night."),
  T("## Why Pluto isn't a planet anymore\nIn **2006**, the International Astronomical Union defined a planet as a body that:\n\n1. **orbits the Sun**,\n2. is massive enough to pull itself **round**, and\n3. has **cleared its orbit** of other similar-sized objects.\n\nPluto passes 1 and 2, but it shares its region with many other Kuiper Belt objects, so it fails rule 3. It's now classified as a **dwarf planet**, alongside Eris, Ceres and others."),
  T("## Gravity and weight\nYour **mass** (how much matter you have) is the same everywhere. Your **weight** (the pull of gravity on you) changes with where you stand.\n\n| Place | Gravity compared to Earth | 180 lb on Earth weighs… |\n|---|---|---|\n| Moon | about 1/6 (0.17) | ~30 lb |\n| Mars | about 0.38 | ~68 lb |\n| Jupiter (cloud tops) | about 2.5 | ~455 lb |\n\nGravity also creates **tides**. The Moon pulls hardest on the side of Earth facing it and weakest on the far side, stretching the oceans into two bulges. Earth rotates through both, so most coasts get **two high tides a day**."),
  T("## Seasons: it's the tilt, not the distance\nEarth's axis is tilted about **23.5°**. As Earth orbits, that tilt stays pointed the same direction in space.\n\n- In **June**, the Northern Hemisphere leans **toward** the Sun: sunlight hits more directly and days are longer. **Summer.**\n- In **December**, it leans **away**: slanted sunlight, short days. **Winter.**\n- The Southern Hemisphere gets the **opposite** season at the same time.\n\n**Proof that distance isn't the cause:** Earth is actually **closest** to the Sun in early **January**, in the middle of northern winter."),
  CHECK("When it's summer in Florida, in Australia it's…", ["summer", "winter", "spring", "the same season everywhere"], 1, "Opposite hemispheres lean opposite ways."),
  T("## Moon phases and eclipses\nThe Moon makes no light. We see sunlight reflecting off it. As it orbits Earth (about every **29.5 days** from new moon to new moon), we see different amounts of its **sunlit half**:\n\n**new → waxing crescent → first quarter → waxing gibbous → full → waning gibbous → third quarter → waning crescent → new**\n\n*Waxing* = growing; *waning* = shrinking.\n\nPhases are **not** caused by Earth's shadow. That only happens during an **eclipse**:\n- **Lunar eclipse:** Earth passes between the Sun and the Moon, and Earth's shadow falls on the Moon (only at **full** moon).\n- **Solar eclipse:** the Moon passes between the Sun and Earth, and its shadow falls on Earth (only at **new** moon)."),
  E("How long does light take?", "The Moon is about 384,000 km away. Light travels about 300,000 km per second. How long does moonlight take to reach you?",
    ["384,000 ÷ 300,000 = 1.28."], "**About 1.3 seconds.** Radio signals to Apollo astronauts had the same delay each way, so conversations had a noticeable pause."),
  N("Common traps", "- **Seasons come from tilt**, not distance.\n- **Phases aren't Earth's shadow.** Only eclipses are.\n- **Space isn't zero gravity.** Astronauts on the space station float because they're constantly **falling** around Earth, not because gravity is gone (it's about 90% as strong up there).\n- **Mass ≠ weight.**")
 ],
 "practice": [
  MC("The largest planet is…", ["Saturn", "Jupiter", "Neptune", "Earth"], 1, "More than twice the mass of all other planets combined."),
  MC("The hottest planet is…", ["Mercury", "Venus", "Mars", "Jupiter"], 1, "Its greenhouse effect beats Mercury's closeness."),
  MC("One astronomical unit (AU) is…", ["the distance to the Moon", "Earth's average distance from the Sun", "a light-year", "the Sun's diameter"], 1, "About 150 million km."),
  MC("Seasons happen because…", ["Earth's distance from the Sun changes", "Earth's axis is tilted", "the Sun gets hotter in summer", "the Moon blocks sunlight"], 1, "About 23.5°."),
  MC("Pluto was reclassified in 2006 because it…", ["isn't round", "doesn't orbit the Sun", "hasn't cleared its orbit", "is made of ice"], 2, "It shares the Kuiper Belt with many similar bodies."),
  NUM("A 150 lb person on Earth weighs about how many pounds on the Moon (use 1/6)?", 25, "150 ÷ 6 = 25.", unit="lb"),
  MC("A lunar eclipse can only happen at…", ["new moon", "full moon", "first quarter", "any phase"], 1, "Earth must be between the Sun and Moon."),
  MC("*Waxing* means the visible Moon is…", ["shrinking", "growing", "full", "invisible"], 1, "Growing toward full."),
  NUM("Light travels 300,000 km/s. The Sun is 150,000,000 km away. How many **seconds** does sunlight take to reach Earth?", 500,
      "150,000,000 ÷ 300,000 = **500 seconds**, about 8 minutes 20 seconds.",
      level="challenge", hint="Distance ÷ speed = time.", unit="s"),
  NUM("Mars's gravity is about 0.38 of Earth's. A 200 lb fighter would weigh about how many pounds there?", 76,
      "200 × 0.38 = **76 lb**. His mass hasn't changed at all, only gravity's pull.",
      level="challenge", hint="Multiply by the gravity ratio.", tol=0.5, unit="lb"),
  MC("Earth is closest to the Sun in early January. What does that prove?", ["January should be the hottest month everywhere", "Distance from the Sun isn't what causes seasons", "The Sun is hotter in January", "Earth's orbit is a perfect circle"], 1,
     "If distance caused seasons, the whole planet would have summer in January. Instead the north has winter, so tilt must be the cause.",
     level="challenge", hint="If distance mattered most, what would January be like in the north?"),
  MC("Why are there usually **two** high tides a day, not one?", ["The Sun and Moon each cause one", "The Moon's pull stretches Earth's oceans into two bulges, one on each side, and Earth rotates through both", "Wind pushes water twice", "Earth wobbles twice a day"], 1,
     "The near side is pulled more than Earth's center, and the center more than the far side. That stretch makes two bulges.",
     level="challenge", hint="Gravity gets weaker with distance. Think about the near side, the center and the far side."),
 ],
 "sources": [AST, NASA, {"title": "IAU 2006 General Assembly: Result of the IAU Resolution votes", "url": "https://www.iau.org/IAU/Iau/News/PR2006/iau-2006-general-assembly-resolution-votes.aspx"}]})

# ---------------------------------------------------------------- Stars, galaxies and the universe
L.append({"id": "stars-galaxies-and-the-universe", "title": "Stars, galaxies and the universe", "band": "Grades 7–8", "minutes": 34,
 "lede": "How stars shine, live and die, why you're made of material forged inside them, and how we know the universe began 13.8 billion years ago.",
 "sections": [
  T("## What a star is\nA **star** is a giant ball of hot gas held together by its own gravity. In its **core**, pressure and temperature are so extreme (the Sun's core is about **15 million °C**) that hydrogen atoms smash together and fuse into **helium**. That's **nuclear fusion**.\n\nFusion converts a tiny bit of mass into a huge amount of energy, which is what Einstein's **E = mc²** describes: energy equals mass times the speed of light squared. Because c² is enormous, a little mass makes a lot of energy. The Sun turns about **4 million tons** of mass into energy **every second**, and it has enough fuel to keep going for billions of years.\n\nA star's life is a balance: **gravity** squeezes inward; the **energy from fusion** pushes outward."),
  T("## Reading a star's color\nA star's color tells you its **surface temperature**, the same way a stove burner glows red, then orange, then white as it heats up.\n\n| Color | Surface temperature | Example |\n|---|---|---|\n| red | ~3,000 °C (coolest) | Betelgeuse, most small stars |\n| orange | ~4,000 °C | Arcturus |\n| yellow-white | ~5,500 °C | the Sun |\n| white | ~10,000 °C | Sirius |\n| blue | 20,000 °C+ (hottest) | Spica |\n\nSurprising to most people: **blue stars are hotter than red ones**."),
  CHECK("Which star is hottest at its surface?", ["a red star", "an orange star", "a yellow star", "a blue star"], 3, "Blue = hottest; red = coolest. The opposite of the hot/cold colors on a faucet."),
  T("## The life of a star: mass decides everything\nEvery star is born in a **nebula**, a cloud of gas and dust, when gravity pulls a clump together until its core ignites fusion.\n\n**Sun-like stars:**\n**nebula → main-sequence star** (fusing hydrogen for billions of years) **→ red giant** (swells up as the core runs low) **→ planetary nebula** (outer layers drift away) **→ white dwarf** (a hot, Earth-sized leftover core that slowly cools)\n\n**Massive stars** (more than about 8 times the Sun):\n**nebula → main sequence** (shorter: they burn fuel much faster) **→ red supergiant → supernova** (a colossal explosion that can briefly outshine a whole galaxy) **→ neutron star** or, for the biggest, **black hole**\n\nThe Sun is about **4.6 billion years** old, roughly halfway through its life. In about 5 billion years it will become a red giant."),
  T("## You are made of star stuff\nThe Big Bang produced mostly **hydrogen and helium**. Nearly all the heavier elements, the **carbon** in your cells, the **oxygen** you breathe, the **calcium** in your bones and the **iron** in your blood, were made later, by fusion inside stars and in their explosive deaths, then scattered into space to form new stars and planets.\n\nAstronomer Carl Sagan put it simply: *we are made of star-stuff.* That's not poetry. It's chemistry."),
  T("## Measuring cosmic distance\nA **light-year** is a **distance**, not a time: how far light travels in one year, about **9.5 trillion km** (5.9 trillion miles).\n\n- The nearest star beyond the Sun, **Proxima Centauri**, is about **4.2 light-years** away. Its light left before you finished your last few birthdays.\n- Looking far is looking **back in time**. You see stars as they were when their light left them."),
  T("## Galaxies\nA **galaxy** is a vast system of stars, gas, dust and dark matter held together by gravity.\n\n- Our galaxy, the **Milky Way**, is a **barred spiral** about **100,000 light-years** across, with **hundreds of billions** of stars. The Sun sits in a spiral arm about 26,000 light-years from the center, where a supermassive black hole sits.\n- Galaxy shapes: **spiral** (pinwheel), **elliptical** (smooth, oval), **irregular** (no clear shape).\n- Our nearest large neighbor, the **Andromeda Galaxy**, is about **2.5 million light-years** away. On a dark night it's one of the most distant things you can see with your naked eyes, and the light you see left it before our species existed.\n- The observable universe holds **hundreds of billions** of galaxies, possibly more."),
  T("## The Big Bang\nAbout **13.8 billion years ago**, the universe was extremely hot and dense, and it has been **expanding** and cooling ever since. Three key pieces of evidence:\n\n1. **Galaxies are moving apart.** In 1929, **Edwin Hubble** showed that farther galaxies are moving away faster. Their light is stretched toward red (**redshift**), like the falling pitch of a passing siren. Run the movie backward and everything was once together.\n2. **The cosmic microwave background.** In 1965, Arno Penzias and Robert Wilson detected a faint microwave glow coming from every direction: the cooled-down afterglow of the early hot universe.\n3. **The mix of elements.** The amounts of hydrogen and helium in the universe match what the Big Bang theory predicts.\n\nIt wasn't an explosion **inside** space. It was the expansion **of space itself**, everywhere at once."),
  E("How old is the light?", "A galaxy is 50 million light-years away. When did the light you see today leave it?", ["A light-year is the distance light travels in a year.", "50 million light-years away → the light traveled 50 million years."], "**50 million years ago**, after the dinosaurs died out (about 66 million years ago). If that galaxy vanished today, we wouldn't know for 50 million years."),
  N("Common traps", "- **A light-year is a distance**, not a time.\n- **Stars don't burn like fire.** Fire is chemical; stars are nuclear fusion. Space has no oxygen for fire.\n- **Black holes aren't cosmic vacuum cleaners.** From far away, a black hole's gravity acts like any object of the same mass. If the Sun became one (it can't: too small), Earth's orbit wouldn't change.\n- **The Big Bang didn't happen at one point in space.** Space itself expanded.")
 ],
 "practice": [
  MC("Stars produce energy by…", ["burning oxygen", "nuclear fusion of hydrogen into helium", "chemical reactions", "reflecting light"], 1, "Fusion in the core."),
  MC("A light-year measures…", ["time", "distance", "brightness", "speed"], 1, "How far light goes in a year."),
  MC("The Sun will end its life as a…", ["black hole", "neutron star", "white dwarf", "supernova"], 2, "It's not massive enough for a supernova."),
  MC("Our galaxy, the Milky Way, is a…", ["elliptical galaxy", "barred spiral galaxy", "irregular galaxy", "star cluster"], 1, "About 100,000 light-years across."),
  MC("The universe is about how old?", ["6,000 years", "4.6 billion years", "13.8 billion years", "infinitely old"], 2, "4.6 billion is the solar system's age."),
  MC("The cosmic microwave background is…", ["radio signals from aliens", "the afterglow of the early hot universe", "light from the Sun", "noise from Earth's satellites"], 1, "Discovered in 1965."),
  MC("Redshift of distant galaxies shows the universe is…", ["shrinking", "expanding", "standing still", "rotating"], 1, "Hubble, 1929."),
  MC("The iron in your blood was originally made…", ["on Earth", "in the Big Bang", "inside stars and their explosions", "by plants"], 2, "Heavy elements are forged by stars."),
  MC("Star A is red, star B is blue. Which is true?", ["A is hotter", "B is hotter", "They're the same temperature", "Color says nothing about temperature"], 1,
     "Blue = hotter surface, like a flame or a heated piece of metal moving from red to white to blue-white.",
     level="challenge", hint="Think of metal heated in a forge."),
  MC("A massive star burns for about 10 million years; the Sun for about 10 billion. Why does the bigger star die so much sooner?", ["It has less fuel", "Its stronger gravity squeezes the core harder, so it burns its fuel much faster", "It's farther away", "It's made of different elements"], 1,
     "More mass means more fuel, but the extra gravity drives fusion **so much** faster that it runs out first. Big engines burn fuel fastest.",
     level="challenge", hint="More gravity → more pressure → faster fusion."),
  NUM("Proxima Centauri is 4.2 light-years away. A light-year is about 9.5 trillion km. About how many **trillion** km away is it? (1 decimal)", 39.9,
      "4.2 × 9.5 = **39.9 trillion km**. Even our fastest spacecraft would need thousands of years to get there.",
      level="challenge", hint="Multiply light-years by km per light-year.", tol=0.06, unit="trillion km"),
  MC("If the Sun suddenly vanished, how long until Earth went dark?", ["instantly", "about 8 minutes 20 seconds", "about 1 day", "about 1 year"], 1,
     "The last light already on its way would keep arriving for about 8 minutes 20 seconds. (Gravity's change also travels at light speed, so Earth's orbit wouldn't change until then either.)",
     level="challenge", hint="How long does sunlight take to reach us?"),
 ],
 "sources": [AST, {"title": "NASA Science: Stars", "url": "https://science.nasa.gov/universe/stars/"}, {"title": "NASA Science: Galaxies", "url": "https://science.nasa.gov/universe/galaxies/"}]})

save("science", L)
