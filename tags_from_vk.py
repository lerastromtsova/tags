import vk

def count_tag(tag, start, end):
    session = vk.Session(access_token='881dd9059df7819c11fe3edf3ab5398e642dc6e39dfbaf15e441db129d5bf60ca4520ed9be8b94a3c69d9')
    vk_api = vk.API(session)
    query = vk_api.newsfeed.search(q=tag,start_time=start,end_time=end)
    return(query[0])
