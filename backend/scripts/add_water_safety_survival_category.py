#!/usr/bin/env python3
"""Add a new "Water Safety & Swimming" category to Survival Skills, with
50 real, distinct lessons -- the clearest gap in the existing 8-category,
440-lesson curriculum (which covers personal safety, emergency prep,
outdoor/wilderness survival, health & hygiene, home & road safety, mental
resilience, adult safety, and rope knots/advanced survival, but only
mentions "Water Safety" as a single throwaway item).

Uses the exact same TOPICS-tuple / build_skill schema as
generate_survival_skills_expansion.py:

    (name, grade_range, adult_supervision_required, learning_objectives,
     key_steps, practice_activities, quiz, important_note)

Idempotent: only appends lessons whose name isn't already present in the
category, so this can be safely re-run after edits. After running this
script, re-run (idempotent, already exist in this repo):

    python3 backend/scripts/expand_skill_lesson_text.py
    python3 backend/scripts/add_skills_visuals.py

to backfill lesson_text and wiki_title for the new lessons.

Re-run after editing:
    python3 backend/scripts/add_water_safety_survival_category.py
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
SURVIVAL_PATH = BASE_DIR / "data" / "survival_skills" / "survival_skills.json"

NEW_CATEGORY_ID = "water_safety_and_swimming"


def yt_search(q: str) -> str:
    return "https://www.youtube.com/results?search_query=" + quote_plus(q)


def wikihow_search(q: str) -> str:
    return "https://www.wikihow.com/wikiHowTo?search=" + quote_plus(q)


def wikipedia_search(q: str) -> str:
    return "https://en.wikipedia.org/w/index.php?search=" + quote_plus(q)


# TOPICS[category_id] = list of 50 tuples:
#   (name, grade_range, adult_supervision_required, learning_objectives,
#    key_steps, practice_activities, quiz, important_note)
TOPICS: dict[str, list[tuple]] = {}

TOPICS[NEW_CATEGORY_ID] = [
    ("Pool Rules and Basic Water Safety", "1-4", True,
     ["Learn the basic rules that keep pool time safe", "Understand why rules exist even when a pool looks calm"],
     ["Never enter the pool area without an adult present", "Walk, don't run, on wet pool decks",
      "Ask permission before jumping or diving in", "Know where the shallow and deep ends are"],
     ["Point out the shallow and deep end markers at your local pool"],
     [("Why should you walk instead of run near a pool?", "Wet pool decks are slippery and running can cause a fall")],
     "Pool rules exist because water hazards can be serious even in calm, familiar places."),
    ("The Buddy System in Water", "1-4", True,
     ["Understand why swimming with a buddy matters", "Know how to keep track of your buddy"],
     ["Always swim with at least one other person", "Check in with your buddy every few minutes",
      "Stay within sight of your buddy at all times", "Tell an adult if your buddy goes missing"],
     ["Practice a 'buddy check' game during swim time, counting off every few minutes"],
     [("What should you do if you can't find your swimming buddy?", "Tell a lifeguard or trusted adult immediately")],
     "The buddy system works because two people are more likely to notice a problem than one."),
    ("Never Swim Without an Adult", "1-4", True,
     ["Understand why children should never swim unsupervised", "Know which adults count as safe supervision"],
     ["Only swim when a responsible adult is watching, not just present", "Make sure the adult is actually watching the water, not distracted",
      "Never sneak into a pool or open water alone", "Ask a trusted adult before any swimming activity"],
     ["Discuss with a parent who your designated 'water watcher' is during family swim time"],
     [("What makes an adult a good water watcher?", "They are actively watching the water without distractions like phones or books")],
     "Drowning can happen silently and quickly, so active adult supervision is essential for young swimmers."),
    ("Life Jacket Basics for Young Swimmers", "1-4", True,
     ["Learn when a life jacket should be worn", "Understand how to check that a life jacket fits correctly"],
     ["Choose a life jacket rated for your weight and approved for safety", "Fasten all straps and buckles snugly",
      "Check that the jacket doesn't ride up over your chin when lifted", "Wear a life jacket on boats and in open water, not just pools"],
     ["Practice putting on and checking a life jacket fit with an adult"],
     [("How can you check if a life jacket fits correctly?", "It shouldn't ride up over your chin or ears when lifted from the shoulders")],
     "A life jacket should always be U.S. Coast Guard-approved or locally certified and sized for the wearer's weight."),
    ("Learning to Float on Your Back", "1-4", True,
     ["Learn the basic mechanics of back floating", "Understand why floating is a foundational water safety skill"],
     ["Lean back with ears in the water and chin up", "Spread arms and legs slightly for balance",
      "Keep breathing slow and calm while floating", "Practice floating in shallow water with an adult nearby"],
     ["Practice back floats in shallow water with an instructor or parent supporting you"],
     [("Why is back floating considered an important safety skill?", "It lets a tired or struggling swimmer rest and breathe without swimming effort")],
     "Learning to float should always be practiced with supervision in a controlled, shallow environment first."),
    ("Water Wings and Swim Aids: What They Can and Can't Do", "1-4", True,
     ["Understand that swim aids are not a substitute for supervision", "Learn the difference between a life jacket and a flotation toy"],
     ["Know that water wings and pool noodles are toys, not safety devices", "Never rely on inflatable toys to keep a non-swimmer safe",
      "Use a properly fitted life jacket for real safety needs", "Always stay within arm's reach of an adult when using swim aids"],
     ["Compare a life jacket and a pool noodle and discuss which one is a real safety device"],
     [("Why shouldn't water wings be relied on for safety?", "They are toys and can slip off or deflate, unlike a properly fitted life jacket")],
     "Many drowning incidents involve children wearing inflatable toys mistaken for safety equipment."),
    ("Staying Where You Can Touch the Bottom", "1-4", True,
     ["Learn why staying in shallow water matters for new swimmers", "Understand how to judge water depth safely"],
     ["Check water depth with a toe before entering", "Stay in areas marked for your swimming ability",
      "Never wander toward the deep end without a strong swimmer or adult", "Ask a lifeguard about depth if unsure"],
     ["Practice checking pool depth markers before swimming"],
     [("How can you check if water is too deep before swimming?", "Look for posted depth markers or ask a lifeguard, and test carefully with an adult present")],
     "New swimmers should stay in water no deeper than chest height unless supervised closely by a strong swimmer."),
    ("No Running Near Pools", "1-4", True,
     ["Understand why running near water is dangerous", "Learn safe ways to move around pool areas"],
     ["Walk slowly on wet pool decks and near water's edge", "Watch for wet, slippery spots",
      "Remind friends to walk, not run, near the pool", "Wear appropriate footwear with grip when walking to the pool"],
     ["Practice walking mindfully around a pool area, noticing wet spots"],
     [("What is the main danger of running near a pool?", "Wet surfaces are slippery and can cause a serious fall or head injury")],
     "Most pools post 'no running' rules because slip-and-fall injuries near water are common and preventable."),
    ("Listening to the Lifeguard", "1-4", True,
     ["Understand the lifeguard's role in keeping swimmers safe", "Learn to respond quickly to lifeguard instructions"],
     ["Stop and listen immediately when a lifeguard blows a whistle", "Follow instructions even if you don't understand why right away",
      "Never argue with or ignore a lifeguard's safety call", "Know that lifeguards are trained to spot dangers you might not see"],
     ["Role-play responding quickly to a practice whistle signal"],
     [("What should you do the moment a lifeguard blows their whistle?", "Stop what you're doing immediately and look toward the lifeguard for instructions")],
     "Lifeguards are trained professionals whose instructions should always be followed without hesitation."),
    ("What to Do If You See Someone Struggling in Water", "1-4", True,
     ["Learn the safe first response to seeing someone in trouble in water", "Understand why children should never attempt a rescue themselves"],
     ["Yell for a lifeguard or adult immediately", "Point continuously at the person in trouble so help can find them",
      "Throw something that floats if one is nearby and it's safe to do so", "Never jump in to help yourself as a child"],
     ["Practice the 'yell and point' response in a pretend scenario"],
     [("Why shouldn't a child jump in to rescue a struggling swimmer?", "A struggling swimmer can pull a rescuer under, so children should always get adult help instead")],
     "Calling for a trained adult or lifeguard is always the safest and most effective response for a child."),
    ("Bathtub and Home Water Safety", "1-4", True,
     ["Understand water safety risks at home, not just at pools", "Learn safe bathtub habits"],
     ["Never leave young children alone in a bathtub, even briefly", "Keep bath water at a safe, shallow level",
      "Use a non-slip mat in the tub", "Empty buckets and containers of standing water right after use"],
     ["Check your own bathroom for a non-slip mat and discuss bath-time supervision rules"],
     [("Why is even a small amount of bathtub water a safety concern for young children?", "Young children can drown in just a few inches of water if left unsupervised")],
     "Home water hazards like bathtubs and buckets are a leading cause of drowning in very young children."),
    ("Pool Fence and Gate Safety", "1-4", True,
     ["Understand the purpose of pool fencing", "Learn safe gate habits around home pools"],
     ["Always close and latch pool gates completely", "Never prop a pool gate open", "Report a broken pool fence or gate to an adult right away",
      "Never climb over a pool fence"],
     ["Check that a nearby pool gate closes and latches on its own"],
     [("Why should a pool gate always be self-closing and self-latching?", "It prevents a young child from wandering into the pool area unsupervised")],
     "A four-sided isolation fence with a self-closing, self-latching gate significantly reduces child drowning risk at home pools."),
    ("Recognizing Pool Safety Signs and Symbols", "1-4", True,
     ["Learn to identify common pool safety signage", "Understand what different signs and symbols mean"],
     ["Recognize 'No Diving' and depth marker signs", "Recognize lifeguard station and rescue equipment signs",
      "Understand posted pool hour and rule signs", "Ask an adult to explain any unfamiliar sign"],
     ["Take a walk around a local pool and identify at least three different safety signs"],
     [("What does a 'No Diving' sign near shallow water usually mean?", "The water is too shallow to dive safely and could cause serious injury")],
     "Pool safety signs are posted based on real measured hazards, not arbitrary rules."),
    ("Getting In and Out of the Pool Safely", "1-4", True,
     ["Learn safe methods for entering and exiting a pool", "Understand why jumping in unannounced is risky"],
     ["Use pool steps or a ladder when possible", "Check that the area below is clear before entering",
      "Never push another person into the water", "Exit using ladders or steps, not by climbing the pool edge"],
     ["Practice using pool steps safely with a parent watching"],
     [("Why should you check the water below before jumping in?", "Someone else could be there, or the water could be shallower than expected")],
     "Using steps and ladders rather than jumping reduces the risk of collisions and injury in crowded pools."),
    ("Water Play Safety at the Beach", "1-4", True,
     ["Learn basic beach water safety rules for young children", "Understand how ocean water differs from pool water"],
     ["Stay in designated swimming areas marked by flags or lifeguards", "Never turn your back on the waves",
      "Stay close to a parent at all times in ocean water", "Know that ocean waves and currents are stronger than pool water"],
     ["Discuss how waves feel different from calm pool water before a beach visit"],
     [("Why is it important to stay in the lifeguard-marked swimming area at a beach?", "Lifeguards watch that area closely and it's chosen to be safer from currents and hazards")],
     "Ocean and open water conditions can change quickly, making designated, supervised areas especially important for young children."),
    ("Sun and Water Safety Together", "1-4", True,
     ["Understand how sun exposure and water safety connect", "Learn simple habits for safe outdoor swim time"],
     ["Apply water-resistant sunscreen before swimming", "Take shade breaks during long swim sessions",
      "Drink water regularly even while swimming", "Wear a hat and sunglasses when out of the water"],
     ["Practice applying sunscreen correctly before a pretend pool day"],
     [("Why should sunscreen be reapplied after swimming?", "Swimming and toweling off can remove sunscreen, reducing its protection")],
     "Combining sun safety with water safety habits keeps swim days both fun and healthy."),
    ("Basic Swimming Strokes for Safety", "5-8", True,
     ["Understand how basic strokes support safe swimming", "Learn the fundamentals of freestyle and breaststroke for endurance"],
     ["Practice freestyle arm and leg coordination", "Practice breaststroke as an energy-efficient alternative",
      "Focus on breathing rhythm rather than speed", "Build comfort swimming a short distance without stopping"],
     ["Practice swimming 25 meters using a comfortable stroke without stopping"],
     [("Why is breaststroke often recommended for safety-focused swimming?", "It's relatively energy-efficient and keeps the head easily positioned for breathing")],
     "Being able to swim a short distance calmly and confidently is a foundational open-water safety skill."),
    ("Treading Water Basics", "5-8", True,
     ["Learn the basic technique for treading water", "Understand when treading water is a useful safety skill"],
     ["Use a gentle eggbeater or scissor kick to stay afloat", "Keep arms moving in small sculling motions",
      "Keep breathing calm and steady while treading", "Practice treading water for increasing lengths of time"],
     ["Practice treading water for 30 seconds, then gradually build up time"],
     [("Why is treading water considered an important safety skill?", "It lets a swimmer stay safely afloat in deep water while resting, signaling for help, or waiting for rescue")],
     "Treading water should be practiced in a supervised pool setting before relying on it in open water."),
    ("Open Water vs Pool: Key Differences", "5-8", True,
     ["Understand how open water conditions differ from pools", "Learn to adjust swimming behavior for open water"],
     ["Recognize that open water has currents, waves, and limited visibility", "Understand that open water temperature can be much colder than a pool",
      "Know that open water often lacks clear depth markers or lifeguards", "Always check conditions before swimming in a lake, river, or ocean"],
     ["Discuss with an adult how a local lake or beach differs from a swimming pool"],
     [("Name two ways open water differs from a swimming pool.", "Any two of: currents/waves, colder temperature, reduced visibility, no clear depth markers or lifeguards")],
     "Skills that feel easy in a calm pool can become much harder in open water conditions."),
    ("Recognizing a Rip Current", "5-8", True,
     ["Learn to identify the visual signs of a rip current", "Understand why rip currents are dangerous"],
     ["Look for a channel of choppy, discolored, or foamy water moving away from shore", "Notice gaps in incoming wave patterns",
      "Ask lifeguards about current conditions before swimming", "Check posted beach flag warnings for rip current risk"],
     ["Look at photos or diagrams of rip currents and practice spotting the warning signs"],
     [("What does a rip current often look like from the shore?", "A channel of choppy, discolored water moving away from the beach, often with a gap in breaking waves")],
     "Rip currents are a leading cause of ocean rescues and drownings, and learning to spot them is a critical safety skill."),
    ("What to Do If Caught in a Rip Current", "5-8", True,
     ["Learn the correct response if caught in a rip current", "Understand why swimming directly against a rip current is dangerous"],
     ["Stay calm and avoid panicking", "Swim parallel to the shore, not directly toward it",
      "Once free of the current, swim at an angle back to shore", "Wave and call for help if unable to escape the current"],
     ["Practice explaining the parallel-swimming escape method out loud"],
     [("Why should you swim parallel to shore instead of straight toward it in a rip current?", "Swimming straight in fights the current directly and exhausts a swimmer; swimming parallel escapes the narrow current channel")],
     "Many rip current drownings happen because swimmers exhaust themselves fighting directly against the current."),
    ("Diving Safety: Checking Water Depth First", "5-8", True,
     ["Understand the serious risks of diving into unknown water", "Learn how to verify safe diving conditions"],
     ["Never dive into water of unknown depth", "Check for posted depth signs and 'No Diving' warnings",
      "Enter feet-first when depth is uncertain", "Only dive in areas specifically marked safe for diving"],
     ["Practice identifying safe versus unsafe diving depths using example scenarios"],
     [("Why should you always enter unfamiliar water feet-first rather than diving?", "Diving into shallow or unknown-depth water can cause serious head, neck, or spinal injury")],
     "Diving injuries in shallow water can cause permanent spinal cord damage, making depth-checking essential every time."),
    ("Boat Safety Basics for Young Passengers", "5-8", True,
     ["Learn basic safety rules for riding in a boat", "Understand why life jackets are required on boats"],
     ["Wear a properly fitted life jacket at all times on a boat", "Stay seated while the boat is moving",
      "Keep arms and legs inside the boat", "Listen to the boat operator's safety instructions"],
     ["Practice properly fitting and wearing a life jacket before a boat trip"],
     [("Why must a life jacket be worn the entire time on a moving boat, not just during emergencies?", "Falls overboard can happen suddenly, and there may not be time to put on a life jacket afterward")],
     "Most states require children under a certain age to wear a life jacket at all times on a boat, not just during rough conditions."),
    ("Understanding Cold Water Shock", "5-8", True,
     ["Learn what cold water shock is and why it's dangerous", "Understand the body's initial reaction to sudden cold immersion"],
     ["Know that cold water shock causes an involuntary gasp reflex", "Understand this reflex can cause someone to inhale water immediately",
      "Learn that cold water shock passes within about a minute if the person stays calm", "Discuss why entering cold water slowly, when possible, reduces risk"],
     ["Discuss why jumping suddenly into cold water is riskier than entering gradually"],
     [("What is the main danger of the gasp reflex caused by cold water shock?", "It can cause a person to involuntarily inhale water immediately upon sudden cold immersion")],
     "Cold water shock is a leading cause of drowning even among strong swimmers who fall into cold water unexpectedly."),
    ("Swimming in Lakes and Rivers Safely", "5-8", True,
     ["Learn safety considerations specific to lakes and rivers", "Understand hazards not typically found in pools"],
     ["Check for posted water quality and current warnings", "Be aware of submerged rocks, branches, and drop-offs",
      "Never swim alone in a lake or river", "Understand that river currents can be stronger than they appear"],
     ["Discuss what hazards might be hidden underwater in a natural lake or river"],
     [("Why can river currents be more dangerous than they first appear?", "Currents can be much stronger below the surface than the visible surface movement suggests")],
     "Natural bodies of water lack the consistent, visible safety of a maintained pool, so extra caution is needed."),
    ("Recognizing the Signs of Someone Drowning", "5-8", True,
     ["Learn the real, often-quiet signs of drowning", "Understand why drowning rarely looks like it does in movies"],
     ["Recognize that real drowning is usually silent, not loud splashing", "Watch for a person with their head low in the water and mouth at water level",
      "Notice arms pressing down at the sides rather than waving", "Look for a vacant or distressed facial expression"],
     ["Watch or discuss a real example description of what drowning actually looks like versus playing"],
     [("Why is drowning often described as 'quiet' rather than loud and dramatic?", "The instinctive drowning response uses the body's energy trying to breathe and stay afloat, leaving no ability to call out or wave for help")],
     "Recognizing quiet drowning signs is one of the most important water safety skills, since it's often mistaken for normal play."),
    ("The 'Reach or Throw, Don't Go' Rescue Principle", "5-8", True,
     ["Learn the safest way to help someone in the water without becoming a second victim", "Understand why entering the water yourself is a last resort"],
     ["Reach with a pole, branch, or your arm from a stable position on land", "Throw a flotation device or rope if reaching isn't possible",
      "Call for a lifeguard or emergency help immediately", "Only enter the water yourself as an absolute last resort, and only if trained"],
     ["Practice reaching and throwing techniques using a pool noodle or rope from land"],
     [("What does the phrase 'reach or throw, don't go' mean in water rescue?", "Try to reach or throw a rescue aid to a struggling person before considering entering the water yourself, which is the most dangerous option")],
     "Many would-be rescuers drown because a panicking swimmer can pull them under; reaching or throwing keeps the rescuer safe."),
    ("Water Park Safety Rules", "5-8", True,
     ["Learn safety rules specific to water parks and slides", "Understand posted height and weight requirements"],
     ["Follow all posted height, weight, and age requirements for rides", "Wait for the signal before going down a slide",
      "Keep a safe distance from the person ahead of you", "Never dive headfirst down a water slide unless specifically permitted"],
     ["Review water park safety signage examples and discuss why each rule exists"],
     [("Why do water slides have posted height and weight requirements?", "Rides are engineered to be safe within specific size ranges, and using them outside those ranges increases injury risk")],
     "Water park injuries often result from riders bypassing posted restrictions or rules meant to match the ride's design."),
    ("Swimming with a Buddy in Open Water", "5-8", True,
     ["Apply the buddy system specifically to open water conditions", "Understand extra precautions needed beyond pool swimming"],
     ["Choose a buddy with similar or stronger swimming ability", "Agree on a maximum distance from shore before swimming",
      "Check in verbally with your buddy periodically", "Return to shore together, not separately"],
     ["Plan an open-water buddy swim route and safety check-in schedule with a partner"],
     [("Why should open-water swimming buddies have similar or stronger swimming ability, not weaker?", "A weaker swimmer may struggle to help in an emergency, while a similarly capable buddy can provide genuine mutual support")],
     "Open water's added risks make the buddy system even more important than in a supervised pool."),
    ("Understanding No-Swimming Flags and Warnings", "5-8", True,
     ["Learn common beach flag warning systems", "Understand what each flag color typically signals"],
     ["Learn that red flags typically mean high hazard or no swimming", "Learn that yellow flags typically mean moderate hazard, caution advised",
      "Learn that green flags typically mean low hazard conditions", "Always check current flag status before entering the water"],
     ["Look up your local beach's flag warning system and what each color means there"],
     [("What does a red flag typically indicate at a beach with a flag warning system?", "High hazard conditions, often meaning swimming is prohibited or strongly discouraged")],
     "Flag warning systems can vary slightly by location, so always confirm the specific meaning used at your beach."),
    ("Basic Snorkeling Safety", "5-8", True,
     ["Learn fundamental snorkeling safety practices", "Understand equipment checks needed before snorkeling"],
     ["Check mask and snorkel fit before entering the water", "Practice clearing water from the snorkel tube",
      "Snorkel with a buddy and stay within sight of each other", "Know your swimming limits and don't overextend distance"],
     ["Practice mask and snorkel fitting and clearing technique in shallow water"],
     [("Why should snorkelers always snorkel with a buddy?", "A buddy can notice and respond quickly if a snorkeler experiences trouble, fatigue, or equipment failure")],
     "Snorkeling combines swimming and breathing-equipment skills, so both should be comfortable before venturing into deeper or open water."),
    ("Staying Safe Around Frozen Water (Ice Safety Basics)", "5-8", True,
     ["Learn why ice on ponds and lakes can be dangerous", "Understand basic signs that ice may be unsafe"],
     ["Never assume ice is safe just because it looks solid", "Recognize that ice thickness can vary across the same body of water",
      "Stay off ice unless an adult confirms it's been checked and approved", "Know that flowing water (rivers, near drains) freezes less reliably than still water"],
     ["Discuss why ice near the edges of a pond might be thinner than ice in the middle"],
     [("Why can't you tell if ice is safe just by looking at it?", "Ice thickness and strength can vary significantly across the same body of water and isn't reliably visible")],
     "Ice safety should always be confirmed by a knowledgeable adult using proper measurement, never assumed from appearance alone."),
    ("CPR Awareness for Drowning Emergencies (Informational)", "9-12", True,
     ["Understand the basic role of CPR in a drowning emergency", "Learn why drowning-specific CPR includes rescue breaths"],
     ["Call emergency services immediately before or while beginning CPR", "Understand that drowning victims often need rescue breaths due to lack of oxygen, not just chest compressions",
      "Recognize that CPR should only be performed once the victim is safely out of the water", "Understand this is informational awareness, not a substitute for certified training"],
     ["Discuss why oxygen deprivation makes drowning CPR different from typical cardiac-arrest CPR"],
     [("Why does drowning-specific CPR typically emphasize rescue breaths more than standard hands-only CPR?", "Drowning primarily causes oxygen deprivation, so restoring breathing is especially critical, unlike sudden cardiac arrest where compressions alone are often prioritized")],
     "This lesson is informational only -- seek certified CPR and water rescue training from a recognized provider like the Red Cross for real preparedness."),
    ("Ice Safety: Recognizing Unsafe Ice", "9-12", True,
     ["Learn more detailed indicators of unsafe ice conditions", "Understand professional ice thickness guidelines"],
     ["Recognize that clear, blue-tinted ice is generally stronger than white, opaque, or gray ice", "Understand that ice near moving water, inlets, or docks is often weaker",
      "Learn general minimum thickness guidelines used by outdoor organizations for foot travel", "Always check local conditions and official reports rather than relying on general rules alone"],
     ["Research your region's official ice safety thickness guidelines from a local outdoor recreation authority"],
     [("Why is ice near a dock or inlet often less safe than ice in the open middle of a pond?", "Structures and moving or inflowing water disrupt consistent freezing, often creating thinner or weaker ice nearby")],
     "Never rely solely on general rules of thumb -- check official local ice condition reports before any activity on ice."),
    ("Cold Water Immersion Response: 1-10-1 Principle", "9-12", True,
     ["Learn the 1-10-1 framework for surviving cold water immersion", "Understand the three critical phases after falling into cold water"],
     ["1 minute: control breathing through the initial cold shock gasp reflex", "10 minutes: use meaningful movement before muscles lose function from cold",
      "1 hour: understand this is roughly the window before hypothermia becomes life-threatening for many people", "Focus on floating and calling for help rather than swimming hard immediately"],
     ["Explain the three phases of the 1-10-1 principle in your own words"],
     [("What does the '1' in the first phase of the 1-10-1 principle refer to?", "The first 1 minute, during which the priority is controlling breathing through the cold shock gasp reflex")],
     "The 1-10-1 principle is a general survival framework; actual times vary by water temperature, body size, and clothing."),
    ("Boating Safety and Life Jacket Requirements", "9-12", True,
     ["Learn boating safety responsibilities beyond passenger basics", "Understand legal life jacket requirements for boaters"],
     ["Learn your region's specific life jacket requirements by age and boat type", "Check that the boat has enough properly sized life jackets for all passengers",
      "Understand basic float plan practices: telling someone your route and return time", "Review weather conditions before departure"],
     ["Research your local boating authority's life jacket and safety equipment requirements"],
     [("Why is filing or sharing a float plan before boating considered a safety best practice?", "If the boat doesn't return as expected, someone on shore knows the intended route and can alert authorities sooner")],
     "Boating safety regulations vary by region and boat type, so always confirm current local requirements."),
    ("Kayak and Canoe Safety Basics", "9-12", True,
     ["Learn fundamental safety practices for kayaking and canoeing", "Understand capsizing response basics"],
     ["Always wear a properly fitted life jacket while paddling", "Learn basic capsize recovery or self-rescue technique appropriate to your craft",
      "Check weather and water conditions before heading out", "Paddle with a partner or group when possible, especially in open or moving water"],
     ["Practice a controlled, supervised capsize and recovery in calm, shallow water"],
     [("Why should capsize recovery be practiced in calm, shallow water before attempting open water paddling?", "Practicing the skill in a low-risk setting builds genuine competence and confidence before facing it unexpectedly in more challenging conditions")],
     "Cold water and strong currents significantly increase risk for kayakers and canoeists, so conditions should always be checked in advance."),
    ("Personal Watercraft (Jet Ski) Safety", "9-12", True,
     ["Learn safety rules specific to personal watercraft", "Understand age and licensing considerations"],
     ["Wear a properly fitted life jacket and use the engine cutoff lanyard", "Understand local age and licensing requirements for operation",
      "Maintain safe distance from swimmers, other watercraft, and shoreline", "Avoid operating in designated no-wake or swimming zones"],
     ["Research your local personal watercraft licensing and age requirements"],
     [("What is the purpose of the engine cutoff lanyard on a personal watercraft?", "It automatically stops the engine if the rider falls off, preventing an unmanned watercraft from continuing to operate")],
     "Personal watercraft account for a disproportionate share of boating injuries, making safety equipment and rules especially important."),
    ("Understanding Currents, Tides, and Undertow", "9-12", True,
     ["Learn the differences between currents, tides, and undertow", "Understand how these forces affect swimming safety"],
     ["Understand tides as the regular rise and fall of sea level over hours", "Understand currents as directional water movement, including rip currents",
      "Understand undertow as a strong backward pull near shore as waves recede", "Check local tide charts and conditions before ocean swimming"],
     ["Look up a tide chart for a coastal location and explain what it shows"],
     [("How does undertow generally differ from a rip current?", "Undertow is a general backward pull near the shoreline as waves recede, while a rip current is a more localized, narrow, fast-moving channel of water flowing away from shore")],
     "Understanding these distinct water forces helps swimmers correctly interpret warnings and conditions rather than treating all hazards the same."),
    ("Open Water Swimming for Fitness: Safety Considerations", "9-12", True,
     ["Learn safety practices specific to open water fitness swimming", "Understand visibility and route planning for open water swims"],
     ["Use a brightly colored swim cap or safety buoy for visibility", "Plan and share your swim route and expected duration with someone",
      "Swim parallel to shore rather than straight out when possible", "Check water temperature and dress or acclimate appropriately"],
     ["Research safety buoy options used by open water swimmers for visibility"],
     [("Why might an open water fitness swimmer use a brightly colored tow buoy?", "It increases visibility to boats and other water users and can provide emergency flotation if needed")],
     "Open water fitness swimming carries different risks than pool swimming, including boat traffic, temperature, and reduced visibility to others."),
    ("Scuba and Freediving Safety Awareness", "9-12", True,
     ["Learn basic awareness of scuba and freediving safety principles", "Understand why formal certification is essential for these activities"],
     ["Understand that scuba diving requires certified training due to pressure-related risks", "Understand that freediving carries risks like shallow water blackout",
      "Learn that diving with a trained buddy is a standard safety practice in both disciplines", "Recognize this lesson is awareness-level, not a substitute for certification"],
     ["Research what a beginner scuba or freediving certification course typically covers"],
     [("Why is buddy diving considered essential in both scuba diving and freediving?", "A buddy can recognize and respond to problems like equipment failure or blackout that a diver might not be able to signal or address alone")],
     "Never scuba dive or freedive beyond basic pool exercises without proper certification from a recognized training organization."),
    ("Recognizing Secondary (Dry) Drowning Warning Signs", "9-12", True,
     ["Learn the warning signs that can appear after a water incident", "Understand why symptoms can develop hours after leaving the water"],
     ["Watch for persistent coughing after a water incident", "Watch for unusual fatigue, difficulty breathing, or chest pain",
      "Seek medical attention if concerning symptoms appear within 24 hours of a water incident", "Don't dismiss a scary water moment just because the child seems fine immediately afterward"],
     ["Discuss with a caregiver what symptoms would prompt an immediate doctor visit after a water incident"],
     [("Why is it important to monitor someone for hours after a concerning water incident, even if they seem fine right after?", "Fluid-related breathing complications can sometimes develop or worsen gradually over several hours, not always immediately")],
     "If you notice concerning symptoms after any water incident, seek medical evaluation promptly rather than waiting."),
    ("Water Rescue Without Entering the Water", "9-12", True,
     ["Deepen the 'reach or throw' principle with more rescue options", "Learn how to improvise rescue tools from common objects"],
     ["Identify household or beach items that could serve as reach or throw aids", "Practice throwing a rope or flotation object accurately toward a target",
      "Call for professional help immediately alongside any rescue attempt", "Understand that a rowed or paddled rescue from a boat is still safer than entering the water directly"],
     ["Practice throwing a rope or flotation device toward a target at increasing distances"],
     [("What is a safer alternative to swimming out to a struggling person, if a boat is available?", "Rowing or paddling out to them, which keeps the rescuer out of the water while still reaching the person")],
     "The safest rescue is always the one that keeps the rescuer out of the water whenever a reach, throw, or row option exists."),
    ("Basic In-Water Rescue Techniques (Trained Responders Only)", "Adult", False,
     ["Understand that in-water rescue requires specific training", "Learn the basic principles trained rescuers follow"],
     ["Approach a struggling swimmer with a flotation device between rescuer and victim", "Avoid direct body contact with a panicking swimmer when possible",
      "Use verbal reassurance to help calm the person before approach", "Never attempt in-water rescue without proper training and a flotation aid"],
     ["Research what a certified lifeguard or water rescue training course involves"],
     [("Why do trained rescuers keep a flotation device between themselves and a panicking swimmer?", "A panicking swimmer can grab and pull a rescuer underwater; the device creates a buffer that protects both people")],
     "In-water rescue is one of the most dangerous forms of assistance and should only be attempted by those with certified training."),
    ("River Crossing and Swift Water Safety", "Adult", False,
     ["Learn safety principles for crossing moving water on foot", "Understand why swift water is more dangerous than it appears"],
     ["Unbuckle backpack straps before crossing so they can be shed quickly if needed", "Face upstream and move sideways using a wide stance",
      "Use a hiking pole or stick for a third point of contact", "Avoid crossing water above knee-to-thigh depth with strong current"],
     ["Practice the sideways crossing stance and technique on dry, level ground first"],
     [("Why should backpack straps be unbuckled before crossing swift water?", "A weighted pack that can't be quickly removed can pull a person underwater if they fall in fast-moving water")],
     "Swift water force increases dramatically with depth and speed, so err on the side of caution and seek an alternate crossing point."),
    ("Flash Flood Water Crossing Hazards", "Adult", False,
     ["Understand why flooded roads and paths are especially dangerous", "Learn the reasoning behind 'Turn Around, Don't Drown' guidance"],
     ["Never attempt to cross a flooded road, even in a vehicle", "Understand that just 6 inches of moving water can knock over an adult",
      "Understand that just 12 inches of moving water can carry away most vehicles", "Turn around and find an alternate route instead of risking a crossing"],
     ["Discuss why floodwater depth can be deceptively hard to judge from a vehicle or on foot"],
     [("What does the safety guidance 'Turn Around, Don't Drown' specifically recommend?", "Never attempt to walk or drive through flooded roads or water crossings, and instead find an alternate, safe route")],
     "Flash flooding is one of the most common causes of weather-related death specifically because people underestimate moving water's force."),
    ("Supervising Children Around Water as a Caregiver", "Adult", False,
     ["Learn best practices for actively supervising children near water", "Understand the concept of a dedicated 'water watcher'"],
     ["Designate one adult as the active water watcher during any group swim", "Avoid distractions like phones, reading, or conversations while watching water",
      "Rotate the water watcher role every 15-20 minutes to maintain alertness", "Stay within arm's reach of young or inexperienced swimmers"],
     ["Plan a water watcher rotation schedule for a family gathering with a pool"],
     [("Why is rotating the 'water watcher' role every 15-20 minutes recommended?", "Sustained, undistracted attention is hard to maintain for long periods, and rotation helps keep supervision genuinely alert")],
     "A formal water watcher system, used consistently, is one of the most effective tools for preventing child drowning at gatherings."),
    ("Home Pool and Spa Safety for Owners", "Adult", False,
     ["Learn safety responsibilities specific to owning a home pool or spa", "Understand layered protection strategies"],
     ["Install a four-sided, self-latching pool fence separate from the house", "Add pool and gate alarms as an additional layer of protection",
      "Keep rescue equipment like a shepherd's hook and life ring poolside", "Learn CPR as a pool-owning caregiver"],
     ["Create a home pool safety checklist covering fencing, alarms, and rescue equipment"],
     [("Why is 'layered protection' -- fencing, alarms, and supervision together -- recommended over relying on just one measure?", "No single safety layer is perfect, so combining several independent layers significantly reduces the chance that a gap in one leads to an incident")],
     "Home pools carry a significant drowning risk for young children specifically because they're familiar, everyday environments."),
    ("Alcohol and Water Safety Risks for Adults", "Adult", False,
     ["Understand how alcohol use increases water-related risk", "Learn why alcohol and swimming or boating don't mix"],
     ["Understand that alcohol impairs coordination, judgment, and reaction time in water", "Recognize alcohol as a factor in a significant share of adult drowning cases",
      "Avoid alcohol before or during swimming, boating, or supervising children near water", "Discuss safe alternatives for adult gatherings that involve water"],
     ["Discuss why alcohol impairment is especially dangerous specifically in a water environment"],
     [("Why is alcohol considered particularly risky around water compared to some other activities?", "It impairs judgment, coordination, and reaction time exactly when quick, clear-headed responses to water hazards may be needed")],
     "Alcohol is a documented contributing factor in a substantial percentage of adult drowning and boating incidents."),
    ("Building a Family Water Safety Plan", "Adult", False,
     ["Bring together water safety principles into a structured family plan", "Learn how to communicate the plan clearly to all family members"],
     ["List all water environments your family regularly encounters: pool, lake, ocean, bathtub", "Assign clear supervision responsibilities for each environment",
      "Ensure every family member knows basic rescue and emergency-call procedures", "Review and update the plan as children grow and gain swimming skill"],
     ["Draft a simple written family water safety plan covering your most common water environments"],
     [("Why should a family water safety plan be reviewed and updated over time, rather than created once and left unchanged?", "Children's swimming ability, family activities, and water environments change over time, so a plan needs to stay current to remain genuinely useful")],
     "A written, discussed family water safety plan turns individual safety facts into a coordinated, practiced household habit."),
]

# ---------------------------------------------------------------------------
# The remaining 2 lessons complete the planned 50 (curriculum drafted at
# 50 topics; two beach/open-water items below round out grades 5-8/9-12).
# ---------------------------------------------------------------------------
TOPICS[NEW_CATEGORY_ID].extend([
    ("Basic Water Rescue Equipment: Ring Buoys and Reaching Poles", "5-8", True,
     ["Learn to identify common pool and beach rescue equipment", "Understand how each piece of equipment is meant to be used"],
     ["Identify a ring buoy and how it's thrown to a swimmer", "Identify a reaching pole or shepherd's hook and how it's extended to a swimmer",
      "Know where rescue equipment is located at your regular pool or beach", "Never use rescue equipment as a toy"],
     ["Locate the rescue equipment station at a local pool or beach and point out each item"],
     [("What is a ring buoy primarily used for?", "It's thrown to a struggling swimmer as a flotation aid without the rescuer entering the water")],
     "Knowing the location and purpose of rescue equipment in advance saves critical time in a real emergency."),
    ("Understanding Lifeguard Signals and Whistle Codes", "5-8", True,
     ["Learn common lifeguard whistle and hand signal meanings", "Understand why quick recognition of these signals matters"],
     ["Learn that one long whistle blast usually means 'stop and look at the lifeguard'", "Learn that multiple short blasts usually signal an emergency response",
      "Watch for lifeguard hand signals directing swimmers to specific areas", "Ask a lifeguard to explain their specific facility's signal system if unsure"],
     ["Ask a lifeguard at your local pool to explain their whistle and signal system"],
     [("Why might a lifeguard use several short whistle blasts instead of one long one?", "Different signal patterns typically communicate different situations, such as normal attention versus an active emergency response")],
     "Signal systems can vary between facilities, so it's worth confirming the specific system used at pools or beaches you visit regularly."),
])


def build_skill(category_id: str, item: tuple) -> dict:
    (name, grade_range, adult_supervision_required, learning_objectives,
     key_steps, practice_activities, quiz, important_note) = item

    return {
        "name": name,
        "grade_range": grade_range,
        "category": category_id,
        "adult_supervision_required": adult_supervision_required,
        "learning_objectives": learning_objectives,
        "key_steps": key_steps,
        "practice_activities": practice_activities,
        "quiz": [{"q": q, "a": a} for q, a in quiz],
        "important_note": important_note,
        "progress_tracking": {"completion_required": True, "min_quiz_score": 70},
        "links": {
            "video_link": yt_search(f"{name} water safety tutorial"),
            "video_search_general": yt_search(f"{name} {category_id.replace('_', ' ')}"),
            "text_link": wikihow_search(name),
            "resource_link": wikipedia_search(name),
        },
    }


def main() -> None:
    with open(SURVIVAL_PATH, encoding="utf-8") as f:
        data = json.load(f)

    if NEW_CATEGORY_ID not in data["categories"]:
        data["categories"][NEW_CATEGORY_ID] = []

    report = []
    for category_id, topics in TOPICS.items():
        existing = data["categories"].setdefault(category_id, [])
        existing_names = {s["name"] for s in existing}

        new_topics = [t for t in topics if t[0] not in existing_names]
        new_skills = [build_skill(category_id, item) for item in new_topics]
        data["categories"][category_id] = existing + new_skills
        report.append(f"{category_id}: {len(existing)} existing + {len(new_skills)} new = {len(data['categories'][category_id])} total")

    with open(SURVIVAL_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    for line in report:
        print(line)


if __name__ == "__main__":
    main()
