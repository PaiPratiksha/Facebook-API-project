{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang1033{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 6.3.9600}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang9 def common_edu(token) :\par
\tab graph=facebook.GraphAPI(token)\par
\tab profile=graph.get_object("me")\par
\tab friends = graph.get_connections("me", "friends")['data']\par
\par
\tab friends_education = \{ friend['name'] : graph.get_connections(friend['id'], "education")['data'] \par
\tab\tab for friend in friends \}\par
\par
\par
\par
        my_edu = [school['school']['name'] for school in profile['education']]\par
\par
\tab friends_education = [[school['school']['name'] for school in friends_education[name] for name in friends_education]\par
\par
        count = [len(set(f_edu) & set(my_edu)) for f_edu in friends_education]\par
                       \par
        return sum(count)\par
}
 