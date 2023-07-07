### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
<p>Python is used more for back end development while JavaScript is used for Front end development</p>

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  <p>get("c",def_val) and setdefault("c", def_value)</p>

- What is a unit test?
<p>A way of testing the smallest piece of code in a program</p>

- What is an integration test?
<p>A way of testing how to different units work together in a program</p>

- What is the role of web application framework, like Flask?
<p>Flask helps show how to project would run as an application and lets you control the different pages using GET and POST Responses</p>

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  <p> it would be dependent on whether the user can change the type or not/<p>

- How do you collect data from a URL placeholder parameter using Flask?
<p>foods/<pretzel></p>
- How do you collect data from the query string using Flask?
<p>request.query_string</p>

- How do you collect data from the body of the request using Flask?
<p>request.form.get</p>

- What is a cookie and what kinds of things are they commonly used for?
<p>Small text files that help identify your computer</p>

- What is the session object in Flask?
<p>Tracks Session data</p>


- What does Flask's `jsonify()` do?
<p>Returns a response object</p>