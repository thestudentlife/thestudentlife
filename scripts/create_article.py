from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Workflow Login Page
selenium = webdriver.Chrome()
selenium.maximize_window()
selenium.get("http://localhost:8000/workflow/articles/issue/107/")
username = selenium.find_element_by_id("id_username")
password = selenium.find_element_by_id("id_password")
username.send_keys("zxiong")
password.send_keys("tsl")
login_submit = selenium.find_element_by_id("login")
login_submit.click()

selenium.implicitly_wait(1)

# Workflow Article Page
create = selenium.find_element_by_id("create-article")
create.click()

# Edit Article Page
title = selenium.find_element_by_id("id_title")
title.clear()
title.send_keys("When Nerdy Becomes Trendy: A New Tack Needed for 5C Hack")

ckeditor = selenium.find_element_by_class_name("cke_wysiwyg_frame")
selenium.switch_to.frame(ckeditor)
content = selenium.find_element_by_tag_name('body')
content.clear()
content.send_keys("""Armed with laptops in one hand and cans of Red Bull in the other, a small stampede of 5C students congregated upon Pomona College’s Lincoln-Edmunds building exactly one week ago, just as the sun was setting. They were gearing up for one of everyone’s most beloved events of the year: The 5C Hackathon.
Every semester, the 5C Hackathon allows students to experience some of the Silicon Valley spirit right here in Claremont. Students come from across the colleges, giving up their Friday night to compete in an overnight contest of app developing, website designing and product building, with the hopes of earning a new pair of headphones or an iPad as a prize.
Tech has suddenly become cool, and geeks along with it. The idea of pulling an all-nighter, hunched over your computer and surrounded by Chipotle wrappers, has never been so romantic. Indeed, we worship it. The rise of online tools like Codecademy, the recent introduction of the Silicon Valley Program at Claremont McKenna College and the extreme overcrowding of the 5C computer science departments is telling: Just about everyone wants to learn how to code.
But with the advent of this newfound popularity comes a serious threat to what hacking has historically represented. Hacking has become mainstream, to be sure, but dangerously so. Hackathons these days, like our own 5C one, have taken on a decidedly bourgeois twist. They have transformed into something wholly antithetical to the original premise of hacking.
Hacking used to be synonymous with creativity or playfulness—actions directed toward operating outside of the system, not reaffirming it. But when you sit hundreds of students down together in a room with an artificial time limit and corporate sponsorship, these virtues begin to wane.
My first hint of that came with the ludicrous swag that was flung upon us when we signed in—think laundry bags embroidered with Google’s logo or shower caps that double as bike seat covers. Then, the fact that the 12-hour event took place overnight, for no apparent reason other than because that is surely what all leet hackers are known to do. And the most obvious clue was perhaps the judging ceremony itself, with its forthrightly corporate orientation. The judges were company recruiters scouting in the flesh, eager to obtain the résumé that we handed in when we registered.
Put it all together, and the Hackathon emerges as an extended job interview designed to tease out those of us who might be elite enough to eventually enroll in a hotbed startup in the north. It is a training ground for future employment, for places where you really might just be expected to work all night, willing or not.
Hacking was once the technological vanguard of society, yet now it is symptomatic of it. Hackathons coopt college students into the workforce track earlier than ever, training them to spend their time in intense sprints of busyness without ever interrogating the implications of that lifestyle.
And 5C students, like college students everywhere, have accepted the gambit. The allure of becoming a hacker shows no signs of stopping, and it is not because people are suddenly more interested in lambda calculus than they were 10 years ago. What our new computer science majors really yearn for is the prospect of a six-figure paycheck right after graduation.
That motive ought to give us liberal arts students a bit of pause. When James Blaisdell wrote, “They only are loyal to this college who, departing, bear their added riches in trust for mankind,” I somehow find it unlikely that he was referring to monetary wealth.
Of course, money is not preclusive of metaphysical happiness. But many mistakenly treat it as a proxy for such. That is an answer that economists might be satisfied with, but I would hope that the rest of the liberal arts know better.
It is true that it would be impossible to host the 5C Hackathon without the financial backing of Bloomberg, Intuit and the like. But we need not dance to the tune of their drum when it starts beating again next November. Cisco and Esri may be steering the ship, but you can choose which way the sails are pointing when you jump onboard.
Supporters of the 5C Hackathon will contend that its true purpose is really to engender learning, mentorship and community building for beginners. And indeed, hackathons do have the potential to bring out incredible shows of innovation and imagination. That is hacking at its best. I have witnessed that joy firsthand at all the hackathons I have attended in my own life since I began coding in high school and in the programming positions that I have held, most recently at BuzzFeed last summer.
But let us just remember that the prizes, the spectating recruiters and the corporate knick-knacks are not emblematic of that spirit—they actually stand in contradiction to it.
""")

selenium.switch_to.default_content()

section_caret = selenium.find_element_by_xpath('/html/body/div/div[1]/form/div[2]/div/span') # Caret
section_caret.click()
section = selenium.find_element_by_xpath('/html/body/div/div[1]/form/div[2]/div/ul/li[3]') # Opinions
section.click()

submit = selenium.find_element_by_id("create")
submit.click()

# WArticle
publish = selenium.find_element_by_id("pub_but")
publish.click()

selenium.get("http://localhost:8000/workflow/logout/")