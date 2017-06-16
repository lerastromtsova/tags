import vk

def count_tag(tag, start, end):
    session = vk.Session(access_token='a359076165df90c2e8eb0525e236fe5b38eaffd7fea441ff43a335b2e5d3d9692cf67ca30305bcd94df30')
    vk_api = vk.API(session)
    query = vk_api.newsfeed.search(q=tag,start_time=start,end_time=end)
    return(query[0])
