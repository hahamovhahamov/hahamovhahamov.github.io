#!/usr/bin/env python3
"""Builds the static site pages into ./site from shared header/footer."""
import json, re
from datetime import date
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent  # repo root (the live site)
NAME = "Renny Hahamovitch"
# Change this to the custom domain (for example https://example.com) once one is connected.
SITE_URL = "https://hahamovhahamov.github.io"
TODAY = date.today()

PAGES = [
    ("index.html", "Home", "A-1"),
    ("research.html", "Research", "A-2"),
    ("publications.html", "Publications", "A-3"),
    ("talks.html", "Talks", "A-4"),
    ("teaching.html", "Teaching", "A-5"),
    ("archive.html", "Archival Highlights", "A-6"),
    ("cv.html", "CV", "A-7"),
]

PLANET = """<svg class="alien" viewBox="0 0 11 11" aria-hidden="true"><rect x="1" y="0" width="1" height="1" fill="#141414"/><rect x="9" y="0" width="1" height="1" fill="#141414"/><rect x="2" y="1" width="1" height="1" fill="#c4412a"/><rect x="8" y="1" width="1" height="1" fill="#c4412a"/><rect x="3" y="2" width="1" height="1" fill="#c4412a"/><rect x="4" y="2" width="1" height="1" fill="#c4412a"/><rect x="5" y="2" width="1" height="1" fill="#c4412a"/><rect x="6" y="2" width="1" height="1" fill="#c4412a"/><rect x="7" y="2" width="1" height="1" fill="#c4412a"/><rect x="2" y="3" width="1" height="1" fill="#c4412a"/><rect x="3" y="3" width="1" height="1" fill="#c4412a"/><rect x="4" y="3" width="1" height="1" fill="#c4412a"/><rect x="5" y="3" width="1" height="1" fill="#c4412a"/><rect x="6" y="3" width="1" height="1" fill="#c4412a"/><rect x="7" y="3" width="1" height="1" fill="#c4412a"/><rect x="8" y="3" width="1" height="1" fill="#c4412a"/><rect x="1" y="4" width="1" height="1" fill="#c4412a"/><rect x="2" y="4" width="1" height="1" fill="#c4412a"/><rect x="3" y="4" width="1" height="1" fill="#c4412a"/><rect x="4" y="4" width="1" height="1" fill="#fbf1d2"/><rect x="5" y="4" width="1" height="1" fill="#fbf1d2"/><rect x="6" y="4" width="1" height="1" fill="#fbf1d2"/><rect x="7" y="4" width="1" height="1" fill="#c4412a"/><rect x="8" y="4" width="1" height="1" fill="#c4412a"/><rect x="9" y="4" width="1" height="1" fill="#c4412a"/><rect x="1" y="5" width="1" height="1" fill="#c4412a"/><rect x="2" y="5" width="1" height="1" fill="#c4412a"/><rect x="3" y="5" width="1" height="1" fill="#fbf1d2"/><rect x="4" y="5" width="1" height="1" fill="#fbf1d2"/><rect x="5" y="5" width="1" height="1" fill="#141414"/><rect x="6" y="5" width="1" height="1" fill="#fbf1d2"/><rect x="7" y="5" width="1" height="1" fill="#fbf1d2"/><rect x="8" y="5" width="1" height="1" fill="#c4412a"/><rect x="9" y="5" width="1" height="1" fill="#c4412a"/><rect x="1" y="6" width="1" height="1" fill="#c4412a"/><rect x="2" y="6" width="1" height="1" fill="#c4412a"/><rect x="3" y="6" width="1" height="1" fill="#c4412a"/><rect x="4" y="6" width="1" height="1" fill="#fbf1d2"/><rect x="5" y="6" width="1" height="1" fill="#fbf1d2"/><rect x="6" y="6" width="1" height="1" fill="#fbf1d2"/><rect x="7" y="6" width="1" height="1" fill="#c4412a"/><rect x="8" y="6" width="1" height="1" fill="#c4412a"/><rect x="9" y="6" width="1" height="1" fill="#c4412a"/><rect x="0" y="7" width="1" height="1" fill="#c4412a"/><rect x="1" y="7" width="1" height="1" fill="#e98a8a"/><rect x="2" y="7" width="1" height="1" fill="#c4412a"/><rect x="3" y="7" width="1" height="1" fill="#c4412a"/><rect x="4" y="7" width="1" height="1" fill="#c4412a"/><rect x="5" y="7" width="1" height="1" fill="#c4412a"/><rect x="6" y="7" width="1" height="1" fill="#c4412a"/><rect x="7" y="7" width="1" height="1" fill="#c4412a"/><rect x="8" y="7" width="1" height="1" fill="#c4412a"/><rect x="9" y="7" width="1" height="1" fill="#e98a8a"/><rect x="10" y="7" width="1" height="1" fill="#c4412a"/><rect x="1" y="8" width="1" height="1" fill="#c4412a"/><rect x="2" y="8" width="1" height="1" fill="#c4412a"/><rect x="3" y="8" width="1" height="1" fill="#c4412a"/><rect x="7" y="8" width="1" height="1" fill="#c4412a"/><rect x="8" y="8" width="1" height="1" fill="#c4412a"/><rect x="9" y="8" width="1" height="1" fill="#c4412a"/><rect x="1" y="9" width="1" height="1" fill="#c4412a"/><rect x="2" y="9" width="1" height="1" fill="#c4412a"/><rect x="3" y="9" width="1" height="1" fill="#c4412a"/><rect x="4" y="9" width="1" height="1" fill="#c4412a"/><rect x="5" y="9" width="1" height="1" fill="#c4412a"/><rect x="6" y="9" width="1" height="1" fill="#c4412a"/><rect x="7" y="9" width="1" height="1" fill="#c4412a"/><rect x="8" y="9" width="1" height="1" fill="#c4412a"/><rect x="9" y="9" width="1" height="1" fill="#c4412a"/><g class="fa"><rect x="1" y="10" width="1" height="1" fill="#c4412a"/><rect x="3" y="10" width="1" height="1" fill="#c4412a"/><rect x="7" y="10" width="1" height="1" fill="#c4412a"/><rect x="9" y="10" width="1" height="1" fill="#c4412a"/></g><g class="fb"><rect x="0" y="10" width="1" height="1" fill="#c4412a"/><rect x="3" y="10" width="1" height="1" fill="#c4412a"/><rect x="7" y="10" width="1" height="1" fill="#c4412a"/><rect x="10" y="10" width="1" height="1" fill="#c4412a"/></g></svg>"""


JSON_LD = json.dumps({
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Renny Hahamovitch",
    "alternateName": "Reynolds Hahamovitch",
    "jobTitle": "PhD Candidate in History and Science & Technology Studies",
    "affiliation": {"@type": "CollegeOrUniversity", "name": "University of Michigan"},
    "alumniOf": [
        {"@type": "CollegeOrUniversity", "name": "University of Michigan"},
        {"@type": "CollegeOrUniversity", "name": "Central European University"},
        {"@type": "CollegeOrUniversity", "name": "College of William & Mary"},
    ],
    "knowsLanguage": ["English", "Yiddish", "Russian"],
    "url": SITE_URL + "/",
    "image": SITE_URL + "/headshot.jpg",
    "sameAs": ["https://lsa.umich.edu/history/people/graduate-students/hahamovi.html"],
}, ensure_ascii=False)

def page(fname, title, body, desc, root="", noindex=False):
    """root is "" for normal pages and "/" for 404.html, which can be served from any depth."""
    tabs = "\n".join(
        f'      <li><a href="{root}{f}"{" aria-current=\"page\"" if f == fname else ""}>{t}</a></li>'
        for f, t, _ in PAGES
    )
    if fname == "index.html":
        full_title = NAME
    else:
        full_title = f"{title} | {NAME}"
    url = SITE_URL + ("" if fname in ("index.html", "404.html") else "/" + fname)
    if fname == "index.html":
        url = SITE_URL + "/"
    robots = '<meta name="robots" content="noindex">\n' if noindex else ""
    canonical = "" if noindex else f'<link rel="canonical" href="{url}">\n'
    ld = f'<script type="application/ld+json">{JSON_LD}</script>\n' if fname == "index.html" else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{full_title}</title>
<meta name="description" content="{desc}">
{robots}{canonical}<meta property="og:type" content="{'profile' if fname == 'index.html' else 'website'}">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE_URL}/headshot.jpg">
<meta property="og:image:width" content="274">
<meta property="og:image:height" content="411">
<meta name="twitter:card" content="summary">
<link rel="icon" type="image/svg+xml" href="{root}favicon.svg">
<link rel="preload" href="{root}fonts/courier-prime-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{root}fonts/silkscreen-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}style.css">
{ld}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="wrap">
  <header class="masthead">
    {PLANET}
    <div class="titles">
      <h1>Renny Hahamovitch</h1>
      <div class="sub">Historian &middot; Science, Technology &amp; Political Economy</div>
    </div>
  </header>
  <nav aria-label="Site">
    <ul class="tabs">
{tabs}
    </ul>
  </nav>
  <main class="folder" id="main">
    <div class="sheet">
{body}
    </div>
  </main>
  <footer>
    <span>&copy; {TODAY.year} Renny Hahamovitch &middot; Ann Arbor, MI</span>
    <span>Last updated {TODAY.strftime("%b.")} {TODAY.day}, {TODAY.year}</span>
  </footer>
</div>
</body>
</html>
"""


HOME = """<div class="intro">
  <figure class="polaroid">
    <span class="tape" aria-hidden="true"></span>
    <img src="headshot.jpg" alt="Portrait of Renny Hahamovitch in front of red autumn leaves" width="274" height="411">
    <figcaption>R.H. &middot; Fall 2026</figcaption>
  </figure>
  <div>
    <p class="lede">I&rsquo;m a historian of 20th century American politics, science &amp; technology, and political economy.</p>
    <div class="contact">
      <span class="k">Transmissions</span>
      <a href="mailto:rnhahamovitch@gmail.com">rnhahamovitch@gmail.com</a>
      <a href="mailto:hahamovi@umich.edu">hahamovi@umich.edu</a>
    </div>
    <div class="buttons">
      <a class="btn primary" href="Hahamovitch-CV.pdf">&#9733; Download CV (PDF)</a>
      <a class="btn" href="https://lsa.umich.edu/history/people/graduate-students/hahamovi.html">U-M History profile</a>
    </div>
    <div class="bio">
      <p>My dissertation, &ldquo;The Space Age: Technological Prophecy and the Political Economy of Big Tech,&rdquo; offers a novel social history of the emergence of the United States as a global space power from the origins of modern rocketry to the end of the Apollo program in 1972.</p>
      <p>I am honored this year to be a Rackham Predoctoral Fellow and a Research Fellow at the Consortium for History of Science, Technology, and Medicine. Last year I was an <a href="https://www.historians.org/award-grant/fellowships-in-aerospace-history/">NASA&ndash;AHA Fellow in Aerospace History</a> which has allowed me to be based partly in Chicago and partly in Washington, DC where I was a resident at the <a href="https://www.loc.gov/programs/john-w-kluge-center/about-this-program/">Kluge Center</a>. I was also the recipient of the Gerald R. Ford Scholar Award in Honor of Robert M. Teeter and the Reed Fink Award in Southern Labor History.</p>
      <p>In 2024 I was a fellow at Middlebury&rsquo;s <a href="https://www.middlebury.edu/institute/academics/centers-initiatives/monterey-initiative-russian-studies/mssr-2024">Monterey Symposium</a> in Armenia, Georgia, and Turkey and before that I was a <a href="https://rackham.umich.edu/professional-development/rackham-doctoral-intern-fellowship-program/">Rackham Doctoral Intern Fellow</a> with the <a href="https://nhalliance.org/">National Humanities Alliance</a> where I helped advocate for the humanities in higher education.</p>
      <p>Before coming to Michigan, I was a <a href="https://archivum.org/academics/visegrad-scholarship-at-osa">Visegrad Fellow</a> at the <a href="https://www.archivum.org/">Open Society Archivum</a> in Budapest, which set me on the track of being a historian of space and the Cold War. I have also been supported in my dissertation research by fellowships from Georgia State University, the Kosciuszko Foundation, the FLAS Program, my department, and the University of Michigan.</p>
      <p>I also work alongside Professors <a href="https://lsa.umich.edu/history/people/emeritus/hbrick.html">Howard Brick</a>, <a href="https://www.laroche.edu/Templates/DirectoryDetailFaculty.aspx?id=3600">Paul Le Blanc</a>, and <a href="https://arts-sciences.buffalo.edu/romance-languages-literatures/faculty/departmental-faculty/whitener-brian.html">Brian Whitener</a> on a (massive!) historical document collection called <em>Independent Marxism in the American Century</em>, four volumes of which are forthcoming with Haymarket Books and Brill.</p>
      <p>Before Michigan, I lived in Budapest, Hungary where I received an MA in Comparative History and Jewish Studies from Central European University (now unfortunately forcibly exiled to Vienna). At CEU I completed a thesis entitled &ldquo;Toward the Jewish Revolution: Yiddish Anarchists in New York City, 1901-1906,&rdquo; which traced how Yiddish radicals at the turn of the century went from rejecting to embracing ethnic Jewish politics between the assassination of President William McKinley by anarchist Leon Czolgosz in 1901 to the wave of anti-Semitic pogroms in the Russian empire around the failed 1905 Russian Revolution.</p>
      <p>It won the Peter Hanak Prize for Best Thesis and part of it was republished in <em>With Freedom in Our Ears: Histories of Jewish Anarchism</em>, eds. Anna Elena Torres and Kenyon Zimmer (University of Illinois Press, 2023). That project was supported by CEU and by the Ruth B. Fein Prize from the American Jewish Historical Society. Between my MA and PhD I was a high school teacher in Hungary and an Assistant Managing Editor at Central European University Press.</p>
      <p class="ps">In my spare time I enjoy cooking and patronizing dive bars that struggle to pass health inspections.</p>
    </div>
  </div>
</div>"""

RESEARCH = """<h2>Research</h2>
<div class="mission">
  <span class="k">Dissertation &middot; PhD expected Oct. 2026</span>
  <span class="title">The Space Age: Technological Prophecy and the Political Economy of Big Tech</span>
</div>
<p class="note">Committee: <a href="https://lsa.umich.edu/history/people/faculty/mlassite.html">Matthew Lassiter</a>, <a href="https://lsa.umich.edu/history/people/faculty/pselcer.html">Perrin Selcer</a>, <a href="https://fordschool.umich.edu/faculty/joy-rohde">Joy Rohde</a>, <a href="https://lsa.umich.edu/history/people/emeritus/rgsuny.html">Ronald Grigor Suny</a></p>
<p>My dissertation, &ldquo;The Space Age: Technological Prophecy and the Political Economy of Big Tech,&rdquo; offers a novel social history of the emergence of the United States as a global space power from the origins of modern rocketry to the end of the Apollo program in 1972.</p>

<h3>Fields</h3>
<ul class="bullets">
  <li>Modern American History</li>
  <li>Science &amp; Technology Studies</li>
  <li>Modern Russian History</li>
  <li>Urban History and Class Theory</li>
</ul>

<h3>Articles in preparation</h3>
<ul class="bullets">
  <li>&ldquo;Orbital Vision and the Surveillant Sciences: The Co-Adoption of Remote Sensing Satellites by American Intelligence and Urban Planners&rdquo;</li>
  <li>&ldquo;Looking Down: The Production of Intelligence, Fact, and Fiction through Satellite Remote Sensing&rdquo;</li>
  <li>&ldquo;Space Age Blight: How Satellites Reinvented Urban Decay and Urban Redevelopment&rdquo;</li>
  <li>&ldquo;The Martini, A Labor History: Or, the postwar labor accord never existed, but if it did, it was a cocktail&rdquo;</li>
  <li>&ldquo;Cosmic Lunatics: Insanity, Masculinity, and Sexuality in Early Bioastronautics&rdquo;</li>
</ul>

<h3>Earlier work</h3>
<p>My MA thesis at Central European University, &ldquo;Toward the Jewish Revolution: Yiddish Anarchists in New York City, 1901&ndash;1906,&rdquo; won the Peter Hanak Prize for Best Thesis.</p>

<h3>In the press</h3>
<ul class="entries">
  <li><span class="when">Aug. 2026</span><span>Kaitlyn Gastineau, &ldquo;<a href="https://www.midstory.org/the-midwests-hidden-role-in-space-exploration/">The Midwest&rsquo;s Hidden Role in Space Exploration</a>,&rdquo; <em>Midstory</em>, Aug. 10, 2026.</span></li>
  <li><span class="when">May 2026</span><span>James Dau, &ldquo;<a href="https://rackham.umich.edu/discover-rackham/full/funding-the-final-frontier/">Funding the Final Frontier</a>,&rdquo; <em>Discover Rackham</em>, May 19, 2026.</span></li>
</ul>"""

PUBS = """<h2>Publications</h2>

<h3>Journal articles</h3>
<ul class="entries">
  <li><span class="when">2026</span><span>Renny Hahamovitch, R&eacute;ka G&aacute;l, Eleanor S. Armstrong, and Asif Siddiqi, &ldquo;<a href="https://www.tandfonline.com/doi/full/10.1080/09505431.2026.2655707">Dictators of the Future: Tech Oligarchy in Outer Space</a>,&rdquo; <em>Science as Culture</em> 35, no. 3 (2026), Tech Oligarchy Forum, Part 1.</span></li>
</ul>

<h3>Book chapters</h3>
<ul class="entries">
  <li><span class="when">2023</span><span>&ldquo;The Storm of Revolution: The <em>Freie Arbeiter Stimme</em> Reports on the Russian Revolution of 1905,&rdquo; in <a href="https://academic.oup.com/illinois-scholarship-online/book/55620"><em>With Freedom in Our Ears: Histories of Jewish Anarchism</em></a>, ed. Anna Elena Torres and Kenyon Zimmer (University of Illinois Press, 2023).</span></li>
</ul>

<h3>Edited document collections</h3>
<p class="note">With Howard Brick, Paul Le Blanc, and Brian Whitener. Series: <em>Dissident Marxism in the United States</em> (Brill and Haymarket Books).</p>
<ul class="entries">
  <li><span class="when">In press</span><span><em>Leftward Ho! Independent Marxism in the American Century, 1928&ndash;48</em>, vol. 1, <em>Capital&rsquo;s Crisis and Marxist Responses</em>.</span></li>
  <li><span class="when">In press</span><span><em>Leftward Ho! Independent Marxism in the American Century, 1928&ndash;48</em>, vol. 2, <em>Culture, War, and the Crisis of Marxism</em>.</span></li>
  <li><span class="when">In press</span><span><em>Independent Marxism in the American Century, 1949&ndash;1965</em>, vol. 1, <em>Making Sense of New Realities</em>.</span></li>
  <li><span class="when">In press</span><span><em>Independent Marxism in the American Century, 1949&ndash;1965</em>, vol. 2, <em>Re-emergence of Active Struggle and a New Left</em>.</span></li>
</ul>

<h3>Translations</h3>
<ul class="entries">
  <li><span class="when">2023</span><span>Hillel Solotaroff, &ldquo;<a href="https://files.press.uillinois.edu/books/supplemental/p087141/DOC_4_Hillel_Solatorff,_Serious_Questions.pdf">Serious Questions</a>,&rdquo; from <em>Geklibene Shriften: Driter Band</em> (New York, 1924), translated from Yiddish in <a href="https://academic.oup.com/illinois-scholarship-online/book/55620"><em>With Freedom in Our Ears</em></a> (University of Illinois Press, 2023).</span></li>
</ul>

<h3>Public writing</h3>
<ul class="entries">
  <li><span class="when">2023</span><span>&ldquo;<a href="https://lefteast.org/us-military-used-illegal-spy-balloons/">The US Military Has Used Illegal Spy Balloons for Decades</a>,&rdquo; <em>LeftEast</em>, Apr. 4, 2023.</span></li>
</ul>"""


def ent(when, text, video=None):
    t = text
    if video:
        t += ' <span class="tag">video</span>'
    return f'  <li><span class="when">{when}</span><span>{t}</span></li>'


INVITED = [
    ("Jan. 2026", "&ldquo;Machinist on the Moon: The Dreams of Space Age Labor Relations and How They Failed,&rdquo; NASA History Office"),
    ("Apr. 2025", "&ldquo;Machinists on the Moon,&rdquo; Kluge Center, Library of Congress"),
    ("Sep. 2024", "&ldquo;<a href=\"https://www.youtube.com/watch?v=vokSNiu_W4Q\">The Space Age on Strike</a>,&rdquo; Georgia State University Special Collections", 1),
    ("Jan. 2019", "&ldquo;<a href=\"https://www.youtube.com/watch?v=OFCCuNDhjy0\">The &lsquo;Time of Storms&rsquo;: New York Yiddish Anarchists from Kishinev to the 1905 Revolution</a>,&rdquo; Yiddish Anarchism: New Scholarship on a Forgotten Tradition, YIVO", 1),
    ("Nov. 2018", "&ldquo;Forward to the Future: Science and Science Fiction in the US and USSR,&rdquo; Open Society Archivum"),
]
CONF = [
    ("Oct. 2026", "&ldquo;Machinists on the Moon: The Hopes and Anxieties of the Space Age Worker,&rdquo; Society for Social Studies of Science, Toronto"),
    ("Sep. 2026", "&ldquo;Totalitarian Envy: How American Planners Copied Soviet Modernity,&rdquo; Socialist Techno-Optimism and Governance of Economic Development, 1955&ndash;1991, Slavic Research Center, Sapporo"),
    ("Jul. 2026", "&ldquo;From Social Discipline to Economic Discipline: Scientific Imperatives in American Bioastronautics,&rdquo; History of Science Society, Edinburgh"),
    ("Jan. 2026", "&ldquo;Machinist on the Moon: The Hope and Anxieties of the Space Age Worker,&rdquo; in &ldquo;Foreign Policy and Organized Labor During the Cold War,&rdquo; American Historical Association, Chicago"),
    ("Nov. 2025", "Chair, &ldquo;Left Perspectives on Method III: Neoliberal/Cultural Turn in Histories of Socialism,&rdquo; ASEEES, Washington, DC"),
    ("Apr. 2025", "&ldquo;The Rise and Fall of the Space Age: The Value of Technological Development and the Shape of the Future in American Capitalism and Soviet Communism,&rdquo; Political Economy and Cultural Forms Conference, Jordan Center, NYU"),
    ("Feb. 2025", "&ldquo;<a href=\"https://www.youtube.com/watch?v=WefRPI8PVXg\">Machinists on the Moon: The Anxieties and Hopes of the Space Age Worker</a>,&rdquo; Cyborg Workers 2.0, European Trade Union Institute, Brussels", 1),
    ("Dec. 2024", "&ldquo;<a href=\"https://www.youtube.com/watch?v=Kkb3m4cjZgU\">Machinists on the Moon: Unions, the Apollo Program, and the Failure of Space Age Labor Relations</a>,&rdquo; Space Perceptions and Realities, UNIVERSEH, University of Toulouse", 1),
    ("Aug. 2024", "&ldquo;Rocket City 1962: The Space Age as Suburban Utopia,&rdquo; in &ldquo;Touching the Void: Tactile Geographies of Spaceports and New Space,&rdquo; Royal Geographical Society, London"),
    ("Jan. 2024", "&ldquo;Spy Satellites,&rdquo; in &ldquo;Senses &amp; Assemblages,&rdquo; Ensnaring Entanglements, U-M Science, Technology, and Society Symposium"),
    ("Nov. 2023", "&ldquo;Ideologies, Bodies, and Machines: Capitalism and Socialism Encounter in Early Bioastronautics,&rdquo; in &ldquo;Socialism or Barbarism II: Socialism and Science,&rdquo; ASEEES"),
    ("Nov. 2023", "&ldquo;Planning for Collapse: NASA, Futurology, and the Loss of the Long-Term in the Apollo Era,&rdquo; State Planning and Private Entrepreneurship in the 20th Century, Princeton Julis-Rabinowitz Center"),
    ("Oct. 2023", "&ldquo;Planning for Progress: NASA, Futurology, and the Loss of the Long-Term in the Apollo Era,&rdquo; Graduate Research in STS Conference (GRISTS), Harvard Kennedy School"),
    ("Oct. 2021", "&ldquo;Future without Limits, Colonialism without Guilt: The L5 Society and the Dreams of Utopian Space Capitalism,&rdquo; Intentional Communities: Real Utopias in History, Universidad Aut&oacute;noma de Madrid"),
    ("Jun. 2019", "&ldquo;The Storm of Revolution: Jewish Anarchists in New York City and the 1905 Russian Revolution,&rdquo; Global Labor Migration Network Conference, International Institute of Social History, Amsterdam"),
    ("Mar. 2019", "&ldquo;Reconciling the Space Race and Space Age: Soviet and American Imaginations of the Future,&rdquo; 2nd Science Fiction and Communism Conference, American University in Bulgaria"),
]
ORG = [
    ("2026", "Coordinator, &ldquo;Against Stagnation: Reform and Flexibility in Late Socialism,&rdquo; Black Sheep Society (Zoom panel)"),
    ("2025", "Coordinator, Black Sheep Society Symposium III: &ldquo;<a href=\"https://www.youtube.com/watch?v=L9pLh1T5RbI\">Remembering Revisionism</a>&rdquo; with Sheila Fitzpatrick, Anna Krylova, Ronald Suny, and Lewis Siegelbaum", 1),
    ("2024", "Co-coordinator, &ldquo;<a href=\"https://www.youtube.com/watch?v=oxnN9XfP40U\">Learning from the Wise: Black Sheep Symposium II</a>&rdquo;", 1),
    ("2024", "Co-coordinator, &ldquo;<a href=\"https://www.youtube.com/watch?v=zT_qBwyvfHs\">Black Sheep Society Symposium I: The Necessity of the Black Sheep</a>&rdquo;", 1),
    ("2024", "Co-coordinator, &ldquo;<a href=\"https://lsa.umich.edu/sts/ensnaring-engagements.html\">Ensnaring Entanglements</a>,&rdquo; University of Michigan STS Symposium"),
    ("2023", "Organizer, panel &ldquo;Socialism or Barbarism II: Socialism and Science,&rdquo; ASEEES"),
    ("2023", "Co-organizer, &ldquo;Insurgents and Intellectuals: Thought and Practice on the Left in US History,&rdquo; U-M History Department"),
    ("2023", "Co-organizer, The Movement of Labor: Migration, Racialization, and Class Struggle on Europe&rsquo;s Southeastern Periphery, LeftEast and Solidarity Network, Tbilisi"),
    ("2022", "Assistant, &ldquo;A Hit Parade of Historical Turns: From a Russian Perspective&rdquo;"),
]


def entries(rows):
    return "<ul class=\"entries\">\n" + "\n".join(ent(*r) for r in rows) + "\n</ul>"


TALKS = f"""<h2>Talks &amp; Conferences</h2>
<p class="note">Talks marked <span class="tag" style="margin-left:0">video</span> have recordings online.</p>
<h3>Invited talks</h3>
{entries(INVITED)}
<h3>Conference presentations</h3>
{entries(CONF)}
<h3>Academic organizing</h3>
{entries(ORG)}"""

TEACHING = """<h2>Teaching</h2>
<h3>University of Michigan</h3>
<ul class="entries nodate">
  <li><span><strong>Russia/USSR in the 20th and 21st Centuries: War, Revolution, and Reform</strong> (Hist 434 / PolSci 434). Teaching assistant for <a href="https://lsa.umich.edu/history/people/emeritus/rgsuny.html">Ronald Grigor Suny</a>.</span></li>
  <li><span><strong>American Addictions</strong> (Hist 305 / PolSci 321). Teaching assistant for <a href="https://lsa.umich.edu/history/people/faculty/cowles.html">Henry Cowles</a>.</span></li>
</ul>
<h3>Lauder Javne School, Budapest</h3>
<ul class="entries nodate">
  <li><span><strong>Jewish History: Jews, Europe, and the City, 1500 to the Present</strong>. Primary instructor.</span></li>
</ul>
<h3>Courses in preparation</h3>
<ul class="bullets">
  <li>Do Machines Dream? Or, the History of the Future</li>
  <li>The Space Age: American Technology and the Vertical Empire</li>
  <li>Modern U.S. Survey</li>
  <li>Modern Russian/Soviet Survey</li>
  <li>Theoretical Approaches to Technology and Society (graduate seminar)</li>
</ul>
<h3>Service</h3>
<ul class="entries">
  <li><span class="when">2021&ndash;23</span><span>Co-coordinator, Science and Technology Studies Rackham Interdisciplinary Workshop</span></li>
</ul>"""

AWARDS = [
    ("2026", "History of Science Society, National Science Foundation Travel Grant"),
    ("2025&ndash;26", "Research Fellow, Consortium for the History of Science, Technology, and Medicine"),
    ("2025&ndash;26", "Rackham Predoctoral Fellow, University of Michigan"),
    ("2025&ndash;26", "William T. Golden Research Fellow, American Philosophical Society <span class=\"note\">(declined)</span>"),
    ("2025&ndash;26", "Smithsonian Predoctoral Fellowship <span class=\"note\">(declined)</span>"),
    ("2025&ndash;26", "U-M Institute for the Humanities Graduate Student Fellow <span class=\"note\">(declined)</span>"),
    ("2024&ndash;25", "Resident Scholar, Kluge Center, Library of Congress"),
    ("2024&ndash;25", "NASA&ndash;AHA Fellow in Aerospace History"),
    ("2024", "Gerald R. Ford Dissertation Scholar Award in Honor of Robert M. Teeter, Ford Library"),
    ("2024", "Ford Presidential Library Research Grant"),
    ("2024", "Rackham Doctoral Intern Fellow, National Humanities Alliance"),
    ("2024", "Monterey Symposium Fellow"),
    ("2023", "Reed Fink Award in Southern Labor History, Georgia State University"),
    ("2023", "Kosciuszko Foundation Tuition Scholarship"),
    ("2021&ndash;22", "FLAS Fellowships, Russian (academic year 2021&ndash;22; summers 2021 and 2022)"),
    ("2018", "Visegrad Fellow, Open Society Archivum"),
    ("2018", "Peter Hanak Prize for Best Master&rsquo;s Thesis, CEU History Department"),
    ("2017", "YIVO Uriel Weinreich Yiddish Summer Program Scholarship"),
    ("2017", "Ruth B. Fein Prize, American Jewish Historical Society"),
    ("2017", "CEU History Department and Jewish Studies Research Grants"),
]

CV = f"""<h2>Curriculum Vitae</h2>
<p>The full CV, with every talk, award, and appointment, is available as a PDF.</p>
<div class="buttons" style="margin-top:0;margin-bottom:8px">
  <a class="btn primary" href="Hahamovitch-CV.pdf">&#9733; Download CV (PDF)</a>
</div>

<h3>Education</h3>
<ul class="entries">
  <li><span class="when">2026</span><span>PhD (expected), History and Science &amp; Technology Studies, University of Michigan</span></li>
  <li><span class="when">2025</span><span>MA, History and Science &amp; Technology Studies, University of Michigan</span></li>
  <li><span class="when">2018</span><span>MA, History, concentration in Jewish Studies, Central European University</span></li>
  <li><span class="when">2016</span><span>BA, summa cum laude, College of William &amp; Mary</span></li>
</ul>

<h3>Fellowships &amp; awards</h3>
{entries(AWARDS)}

<h3>Other experience</h3>
<ul class="entries">
  <li><span class="when">2022&ndash;24</span><span>Acting Editor, <a href="https://lefteast.org/">LeftEast</a></span></li>
  <li><span class="when">2020&ndash;</span><span>Research Assistant to <a href="https://lsa.umich.edu/history/people/emeritus/hbrick.html">Howard Brick</a></span></li>
  <li><span class="when">2024</span><span>Rackham Doctoral Intern Fellow, <a href="https://nhalliance.org/">National Humanities Alliance</a></span></li>
  <li><span class="when">2019</span><span>Assistant Managing Editor, Central European University Press</span></li>
  <li><span class="when">2014&ndash;22</span><span>Copy editor and proofreader for CEU Press, <em>LABOR: Studies in Working-Class History</em>, LeftEast, and Manchester University Press</span></li>
</ul>

<h3>Languages</h3>
<p>English (native) &middot; Yiddish (advanced) &middot; Russian (advanced)</p>

<h3>Memberships</h3>
<p>AHA &middot; OAH &middot; History of Science Society &middot; SHOT &middot; 4S &middot; LAWCHA &middot; ASEEES &middot; Economic History Association</p>"""

from PIL import Image

# (file, kind, title, alt text, credit HTML)
PRINTS = [
    ("laputa-engraving.jpg", "Engraving",
     "Gulliver sees the flying island of Laputa",
     "Engraving of a man in eighteenth-century dress standing on a shore and looking up at a flying island city, with a sailboat beside him",
     'Illustrated German-language edition of Jonathan Swift, <a href="https://www.gutenberg.org/ebooks/829"><em>Gulliver&rsquo;s Travels</em></a> (1726).'),
    ("wood-moon-skeletons.jpg", "Illustration",
     "Explorers among skeletons on the Moon",
     "Two figures in diving-style suits and helmets stand among ruined walls and scattered human skeletons on the Moon under a starry sky",
     'Stanley L. Wood, illustration probably for George Griffith, &ldquo;Stories of Other Worlds,&rdquo; <em>Pearson&rsquo;s Magazine</em>, 1900, later published as <a href="https://www.gutenberg.org/ebooks/19476"><em>A Honeymoon in Space</em></a> (London: C. Arthur Pearson, 1901).'),
    ("jane-airship.jpg", "Illustration",
     "Airship over a night battlefield",
     "Night scene of a winged airship with searchlights beaming across the sky above a crowd of soldiers, signed Fred T. Jane",
     'Fred T. Jane, illustration probably for George Griffith, <a href="https://www.gutenberg.org/ebooks/31324"><em>The Angel of the Revolution: A Tale of the Coming Terror</em></a> (London: Tower Publishing, 1893).'),
    ("spacecraft-interior.jpg", "Illustration",
     "Travelers in a spacecraft, with the Moon in the windows",
     "Sepia illustration of two men inside a spacecraft, with a cup and boxes floating in the air and the Moon, stars and a comet visible through large windows",
     'E. Hering, illustration for H. G. Wells, <a href="https://en.wikipedia.org/wiki/The_First_Men_in_the_Moon"><em>The First Men in the Moon</em></a>, serialized in <em>Cosmopolitan</em> (1900&ndash;1901) and published by Bowen-Merrill (Indianapolis, 1901).'),
    ("copenhagen-1807.jpg", "Color print",
     "The burning of the Church of Our Lady, Copenhagen, 1807",
     "Hand-colored print of a Copenhagen street at night with a church tower in flames, streaks of light crossing the sky, and residents fleeing in the foreground",
     'G. L. Lahde, after C. W. Eckersberg, <em>Vor Frue Taarns Brand</em> (<em>The Fire of the Church of Our Lady</em>), color print, 1807. See the Library of Congress <a href="https://www.loc.gov/resource/gdcwdl.wdl_11251/">World Digital Library record</a>.'),
    ("melies-conquete-du-pole.jpg", "Poster",
     "Poster for <em>&Agrave; la conqu&ecirc;te du p&ocirc;le</em>",
     "Color poster showing a fleet of fantastical winged flying machines over polar mountains, with the title at the top",
     'Poster for Georges M&eacute;li&egrave;s, <a href="https://en.wikipedia.org/wiki/The_Conquest_of_the_Pole"><em>&Agrave; la conqu&ecirc;te du p&ocirc;le</em></a> (Paris: Star Film, 1912). See also the Academy Museum&rsquo;s record of the <a href="https://www.academymuseum.org/en/collection/poster-for-melies-a-la-conquete-du-pole">French release poster</a>.'),
]

def _figure(f, kind, title, alt, credit):
    w, h = Image.open(OUT / "images" / f).size
    return f"""<figure class="print">
  <a class="mount" href="images/{f}"><img src="images/{f}" alt="{alt}" width="{w}" height="{h}" loading="lazy"></a>
  <figcaption>
    <span class="kind">{kind}</span>
    <strong class="ptitle">{title}</strong>
    <span class="credit">{credit}</span>
  </figcaption>
</figure>"""

ARCHIVE = """<h2>Archival Highlights</h2>
<p class="note">Select an image to open it at full size.</p>
<div class="gallery">
""" + "\n".join(_figure(*p) for p in PRINTS) + """
</div>"""


DESC = "Renny Hahamovitch, historian of twentieth-century American politics, science and technology, and political economy. PhD candidate, University of Michigan."
BODIES = {
    "index.html": HOME, "research.html": RESEARCH, "publications.html": PUBS,
    "talks.html": TALKS, "teaching.html": TEACHING, "archive.html": ARCHIVE, "cv.html": CV,
}
for f, t, _ in PAGES:
    (OUT / f).write_text(page(f, t, BODIES[f], DESC), encoding="utf-8")

# 404 page, favicon, robots, sitemap
NOT_FOUND = """<h2>Page not found</h2>
<p>That address does not lead anywhere on this site. Use the tabs above, or go back to the <a href="/index.html">Home page</a>.</p>"""
(OUT / "404.html").write_text(
    page("404.html", "Page not found", NOT_FOUND, "Page not found.", root="/", noindex=True), encoding="utf-8")

fav = PLANET.replace('class="alien" ', 'xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges" ').replace(' aria-hidden="true"', "")
fav = re.sub(r'<g class="fb">.*?</g>', "", fav, flags=re.S).replace('<g class="fa">', "").replace("</g>", "")
(OUT / "favicon.svg").write_text(fav, encoding="utf-8")

(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")
urls = "".join(
    f"  <url><loc>{SITE_URL}/{'' if f == 'index.html' else f}</loc><lastmod>{TODAY.isoformat()}</lastmod></url>\n"
    for f, _, _ in PAGES
)
(OUT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n",
    encoding="utf-8")
print("built", len(PAGES), "pages + 404, favicon, robots, sitemap")
