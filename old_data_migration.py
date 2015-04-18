import psycopg2
from workflow.models import Profile
from mainsite.models import Article, Section, Issue

conn = psycopg2.connect("dbname=postgres user=postgres password=794613852")

articles_authors = conn.cursor()
articles = conn.cursor()
authors = conn.cursor()
sections = conn.cursor()
issues = conn.cursor()


def recode(string):
    if string is None:
        return ''
    if string is not str:
        string = str(string)
    string = string.encode('ascii','ignore')
    return string.decode('ascii','ignore')


#save the issues
issues.execute("SELECT * FROM issues")
issues = issues.fetchall()
for issue in issues:
    name = recode(issue[1])
    legacy_id = issue[0]
    created_date = issue[2]
    new_issue = Issue(name=name,legacy_id=legacy_id,created_date=created_date)
    new_issue.save()
    print("Save issue: "+ name)

#save the sections
sections.execute("SELECT * FROM sections")
sections = sections.fetchall()
for section in sections:
    name = recode(section[1])
    legacy_id = section[0]
    priority = section[2]
    new_section = Section(name=name,legacy_id=legacy_id,priority=priority)
    new_section.save()
    print("Save section: "+ name)

#save the authors
authors.execute("SELECT * FROM authors")
authors = authors.fetchall()
for author in authors:
    display_name = recode(author[2])
    legacy_id = author[0];
    position = 'author'
    new_author = Profile(display_name=display_name, position=position,legacy_id=legacy_id)
    new_author.save()
    print("Save author: "+ display_name)

#save all the articles
articles_authors.execute("SELECT * FROM articles_authors")
pair = articles_authors.fetchone()
while True:
    pair = articles_authors.fetchone()
    if pair is None:
        break
    articleID = pair[0]
    authorID = pair[1]
    author = Profile.objects.get(legacy_id=authorID)
    if Article.objects.filter(legacy_id=articleID).exists():
        Article.objects.get(legacy_id=articleID).authors.add(author);
        print("Add an author to article "+str(articleID))
    else:
        articles.execute("SELECT * FROM articles WHERE id = %s", (articleID,))
        article = articles.fetchone()
        issueID = article[5]
        sectionID = article[2]
        section = Section.objects.filter(legacy_id=sectionID)[0]
        if section is None:
            continue
        legacy_id = article[0]
        published = article[7]
        if published is None or published is False:
            continue
        title = recode(article[9])
        if title is None:
            continue
        content = recode(article[6])
        if content is '':
            continue
        issue = Issue.objects.filter(legacy_id=issueID)[0]
        created_date = article[3]
        updated_date = article[4]
        published_date = article[8]
        new_article = Article(
            title=title,
            content=content,
            issue=issue,
            section=section,
            created_date=created_date,
            updated_date=updated_date,
            published_date=published_date,
            published=published,
            legacy_id=legacy_id
        )
        new_article.save()
        print("Add article: "+legacy_id+" "+title)
        new_article.authors.add(author)












