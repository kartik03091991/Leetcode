class Solution:
    def greatestLetter(self, s: str) -> str:
        #65 to 90 uppercase
        #97 to 122 lowercase
        
        #s = "lEeTcOdE"
        #s = "arRAzFif"
        #s = "AbCdEfGhIjK"
        #s="OboRRZWiZWsWbZyoIOSoyZQJYJjRTQTOokbssRbQiWRbizQVVQysyzQdksOQdTTWYysQSVJiRJjYQVYTYTkYjQVZTWdbWQsWZJZbVTJzdbiZVsVQdyyzjOYyOYjSRTZVzjIVoTYiVJzVVZJYJjJbiOVjkbSzSJyYVoIiOydzTYYjOOZOIjkdViYoTkOdosTTkQzSoISSysizoZzyWoRJiVsoiiIVSkYdsjRORyISzQTkdjTosTIVYzSZzkiiSbIQbQVszjYTJsQZIOissQOzOkkzyIzORkYYOVdibOJToJTZOYRRITVyWRjRVOiWisVbyoyOIdoIjTWjsOSjJTVjoiQIyQRibksizsRSjjTzbkOidWRodYikQTTsiJZTYSyYOdbkTdIsVRdVIZJbRiWddiJyJOiJdiJdToQJoiiYiiyoIksIdodbiQkzyYbbOdisbVJYVsTojoTjRIZdQRkJbiQyjbQJOVsYTkjIIiZjdioWVsTZkTzSYYQiOSJbdkObTTZoyJiWoziSojzzkkIYYToOssYTQiWSkbzZjSiTRZbiSyOoziIzkRWzVQjRYQVOjkOsyYjRZozkoOQiZVYsRkRQZkRRQzQRJdORdkdJiIZVzbTSbQQSQzOQOZJkjIdibOkZSzyOVsTIVbJsQYQoRQokVWoWVOydRziYRoyjWWdJzZSTWydzQsVQjIdYTyoOQzksdYIdozViibzbdjoTQYWOQjyOjVJIWbSTQijJozWbkIiZZoSboYZZSbsRORWTSWdsoSTSYTOsdWRRzRVzTORSIsTSVQioQYsyTiYOIZOozQyiOjWkyIQbRTSbYdzyoQOYzyTRYRZdZyIQkSkbJVzsJJoSYJibikTkJizIsYiskzJjQzYSksiQkTVsRbbVIsdzskJOYYszzVdyYTWWQzYJzVROJRJyRTyIRSJTZZiZoVyjQZYRVYjRQosQbbIbsIOSdiZOkk"
  
        
        lstord = []
        
        for x in s:
            a = ord(x)
            lstord.append(a)
        
        #print(lstord)
        
        lstsame = []
        
        for x in range(0,len(lstord)):
            for y in range(0,len(lstord)):
                if abs(lstord[x] - lstord[y]) == 32:
                    lstsame.append(lstord[y])
        
        #print(lstsame)
        s1 = set(lstsame)
        lstsame = list(s1)

        lstsame.sort()
        
        if len(lstsame) == 0:
            return("")
        else:
            a = chr(lstsame[-1])  
            return(a.upper())




"""   
Example 1:

Input: s = "lEeTcOdE"
Output: "E"
Explanation:
The letter 'E' is the only letter to appear in both lower and upper case.
Example 2:

Input: s = "arRAzFif"
Output: "R"
Explanation:
The letter 'R' is the greatest letter to appear in both lower and upper case.
Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.
Example 3:

Input: s = "AbCdEfGhIjK"
Output: ""
Explanation:
There is no letter that
"""