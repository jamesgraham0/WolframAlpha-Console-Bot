import wolframalpha
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

client = wolframalpha.Client('GYAQQE-2Q825JH7J8')


# WolframAlpha Loop that prints to console
while True:
    query = str(input('Query: '))
    res = client.query(query)
    output = next(res.results).text
    print(output)


