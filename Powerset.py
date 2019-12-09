def substrings(arg):
    results = []

    def recurse(build, depth):
        if (depth == len(arg)):
            if build not in results: 
            	results.append(build)
            return

        recurse(build, depth + 1)
        recurse(build + arg[depth], depth + 1)

    recurse('', 0)
    results.remove('')
    return results