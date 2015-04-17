import psycopg2
from workflow.models import Profile
from mainsite.models import Article, Section, Issue

conn = psycopg2.connect("dbname=postgres user=postgres password=794613852")

articles_authors = conn.cursor()
articles = conn.cursor()
authors = conn.cursor()
sections = conn.cursor()

#save the issues
issues = sections.execute("SELECT * FROM issues").fetchall()
for issue in issues:
    name = issue[1]
    legacy_id = issue[0]
    created_date = issue[2]
    new_issue = Issue(name=name,legacy_id=legacy_id,created_date=created_date)
    new_issue.save()
    print("Save issue: "+ name)

#save the sections
sections = sections.execute("SELECT * FROM sections").fetchall()
for section in sections:
    name = section[1]
    legacy_id = section[0]
    priority = section[2]
    new_section = Section(name=name,legacy_id=legacy_id,priority=priority)
    new_section.save()
    print("Save section: "+ name)

#save the authors
authors = authors.execute("SELECT * FROM authors").fetchall()
for author in authors:
    display_name = author[2]
    legacy_id = author[0];
    position = 'author'
    new_author = Profile(display_name=display_name, position=position,legacy_id=legacy_id)
    new_author.save()
    print("Save author: "+ display_name)

#save all the articles
articles_authors.execute("SELECT * FROM articles_authors")
pair = articles_authors.fetchone();
while pair is not None:
    articleID = pair[0]
    authorID = pair[1]
    author = Profile.objects.get(legacy_id=authorID)
    if Article.objects.filter(legacy_id=articleID).exists():
        Article.objects.get(legacy_id=articleID).authors.add(author);
        print("Add an author to article "+articleID)
    else:
        article = articles.execute("SELECT * FROM articles WHERE id = %s", (articleID,)).fetchone()
        issueID = article[5]
        sectionID = article[2]
        section = Section.objects.get(legacy_id=sectionID)
        legacy_id = article[0]
        published = article[7]
        title = article[9]
        content = article[6]
        issue = Issue.objects.get(legacy_id=issueID)
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
        print("Add article: "+title)
        new_article.authors.add(author)















