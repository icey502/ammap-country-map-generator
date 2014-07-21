import re

# currently known tokens and their corresponding regexes
tokens = {"TOKEN1":"easy","TOKEN2":"running fokenize","TOKEN3":"worked great","TOKEN4":"really great"}
TOKEN_REGEX = '\{\{(.+?)}}' # currently, all tokens are of the form {{TOKEN}}

# TODO - in place versus not-in-place option; right now, it is always one file to another file.

def getReplacementTextFor(token, tokenDict):
    """ Returns the replacement for the given token, or None if there is no replacement.
    This is a convenience function to avoid proliferating direct 'tokens' dictionary access all over,
    possibly allowing replacement with another construct. """
    if token in tokenDict:
        return tokenDict[token]
    else:
        return None
        
def lineContainsTokens(line):
    """ returns True if the line contains tokens, and False otherwise. """
    if re.search(TOKEN_REGEX,line):
        return True
    return False
        
# TODO - make sure the target file is removed before running this...
# TODO - add exception handling
def fokenize(infile, outfile, tokenDict, verbose=True):
    """ processes the infile, and produces the outfile; any tokens matching the TOKEN_REGEX with given token values are replaced. """
    replacementCount = 0
    outf = open(outfile, 'w')
    with open(infile) as inf:
        originalLines = 0
        linesWritten = 0
        for line in inf:
            originalLines = originalLines + 1
            lineToWrite = line
            
            # see if there are tokens on the line
            if lineContainsTokens(line):
                snippetStart = 0
                newLine = ""
                for m in re.finditer(TOKEN_REGEX, line): # find {{blah}}
                    # using the returned MatchObject, replace the token if it exists
                    token = m.group(0)[2:-2] # removing the {{}}, reduces things to the bare token
                    if verbose:
                        print ('%02d-%02d: %s' % (m.start(), m.end(), token))
                    tokenLength = len(token)
                    replacement = getReplacementTextFor(token, tokenDict)
                    if replacement:
                        # if we got this far, we replace the token on the line
                        replacementCount = replacementCount + 1
                        tokenStart = m.start()
                        tokenEnd = m.end()
                        # append the segment of the original line, starting from snippetStart to the token, then add the token replacement value...
                        newLine = newLine + line[snippetStart:tokenStart] + replacement
                        #debug only
                        #print("taking snippet '"+line[snippetStart:tokenStart]+"' and replacement '"+replacement+"' from",snippetStart, "to", tokenStart,":",newLine)
                        # next time, continue from the end of the current token
                        snippetStart = tokenEnd
                    
                # get the remainder of the text on the line(which may be nothing if the token is the last element on the line)
                lineToWrite = newLine + line[snippetStart:len(line)]
            linesWritten = linesWritten + 1
            outf.write(lineToWrite) 
    if verbose:                
        print('file: %s | lines read/written: %d/%d | tokens replaced: %d' % (infile, originalLines, linesWritten, replacementCount))

if __name__ == "__main__":
    fokenize("../test_assets/test_file_1.txt","../test_assets/test_file_1_out.txt", tokens)
    fokenize("../test_assets/test_file_2.txt","../test_assets/test_file_2_out.txt", tokens)
    
    