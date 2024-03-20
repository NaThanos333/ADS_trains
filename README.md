 Assignment 5: Trains in the Storm
 It is Friday afternoon, the holidays have just started and you are eager to get there. However,
 there is a slight drizzle, so the Dutch railways have decided to cancel many of the trains.
 How are you going to get to your destination now?
 Below you can see a map of the train lines that are still available.

 In addition to the above, you can get information about additional disruptions, as shown at
 https://www.ns.nl/en/travel-information/current-situation-on-the-tracks.
 This information is included at the beginning of each test case as shown below.
 We make some simplifying assumptions:
 • Weonly care about the duration, not the time of the day.
 • Changing trains never takes any time, all connections are instant.
 • The time required to travel from A to B is the same as from B to A.
 Input
 • The input starts with a line containing the number n of current disruptions.
 • The first line is followed by n many disruptions. Each disruption consists of two lines
 which describe a direct connection that is no longer available.
 • All remaining lines are queries. Each query consists of two lines: the start and the goal.
 • The input ends with an exclamation mark.
 Output
 For each query your program should use Dijkstra’s Algorithm to find the fastest connection
 and then output the list of all stations along that route, including the starting and ending
 station. Moreover, your program should print the total time (in minutes) this connection
 will take. In case there is no connection for a given query, your program should print
 ‘UNREACHABLE’.

 Notes
 • No code is provided for this assignment and no files are automatically included by
 Themis. You may use and construct any data structures you want.
 • Important: Dijkstra’s Algorithm is famous and many implementations can be found
 online. We remind you that submitting any work that is not your own without references
 is plagiarism and all such cases will be forwarded to the Board of Examiners. Instead,
 you are expected to go through the process of designing a functional implementation
 yourself.
 • For the main part of this assignment you can earn up to 3 points by passing the Themis
 tests and up to 2 points for simplicity, efficiency and clarity.
 Report (5 points)
 For this assignment you should also write a programming report. You can find a template
 for this on Brightspace. Please follow all guidelines from Appendix E of the lecture notes
 and submit your report as a single PDF file on Themis.
3
 Extra 1: Optimization with A* (up to 1 bonus point)
 The NS appreciates your program, but it is not efficient enough. Can you optimize it further
 by using the A* algorithm instead of Dijkstra’s Algorithm? For the heuristic you will need
 geo-coordinates of each station. See for example https://osm.org/node/1112410297.
 The input/output format for this part is the same as for the main part of the assignment.
 Extra 2: Going International (up to 1 bonus point)
 Adapt your program to read in an arbitrary train network. The first line of the input is the
 number of different train networks. For each train network, the input then consists of:
 • The number of stations.
 • One line per station, containing a number and the name.
 • The number of connections.
 • One line per connection, listing two stations by their number and the distance in
 minutes.
 • The number of disruptions, followed by two lines for each disruption.
 • Any number of queries, each consisting of two lines.
 • Anexclamation mark after the last query for the current train network.
 
