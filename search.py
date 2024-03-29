# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's   successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    fringe = util.Stack() 
    start_state = problem.getStartState()
    #initial state
    actions = [] 
    #list of the actions that the agent took so far to get to its state(position)
    start_node = (start_state,actions) 
    #node to hold the state(position) and the array of actions
    visited_states = []
    #list of visited states, to avoid redundancy and infinite cycles
    fringe.push(start_node) 

    while not fringe.isEmpty():

        current_node = fringe.pop()
        current_state = current_node[0] 
        #current position
        current_actions = current_node [1] 
        #the actions the agent took so far to get to the current position 


        if (current_state not in visited_states):
            visited_states.append(current_state)

            if (problem.isGoalState(current_state)): 
                #if the current state is the goal return the list of actions
                return current_actions
            
            else:
                successors = problem.getSuccessors(current_state) 
                #list of successors of the current state
                for successor in successors:
                    successor_state = successor[0] 
                    #successor position
                    successor_action = successor[1] 
                    #successor's required action to get to its position
                    actions = current_actions + [successor_action] 
                    #add the action to the action list
                    next_node = (successor_state,actions)
                    fringe.push(next_node) 
    return actions

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    fringe = util.Queue()
    start_state = problem.getStartState()
    #initial state
    actions = [] 
    #list of the actions that the agent took so far to get to its state(position)
    start_node = (start_state,actions) 
    #node to hold the state and the array of actions
    visited_states = []
     #list of visited states, to avoid redundancy and infinite cycles
    fringe.push(start_node) 

    while not fringe.isEmpty():
 
        current_node = fringe.pop()
        current_state = current_node[0] 
        #current position
        current_actions = current_node [1] 
        #the actions the agent took so far to get to the current position 

        if (current_state not in visited_states):
            visited_states.append(current_state)

            if (problem.isGoalState(current_state)): 
                #if goal return the list of actions
                return current_actions
            
            else:
                successors = problem.getSuccessors(current_state) 
                #list of successors of the current state
                for successor in successors:
                    successor_state = successor[0] 
                    #successor position
                    successor_action = successor[1] 
                    #successor's required action to get to its position
                    actions = current_actions + [successor_action] 
                    #add the action to the action list
                    next_node = (successor_state,actions)
                    fringe.push(next_node) 
    
    return actions

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    #we use a priority since we need to chose our next move based on the cost
    #we will push our nodes(), which contains, the state(position),action list,and the cost
    #that has been spent so far to get to its state
    #and the priority is going to be the cost, aka the next explored node is the one with the least cost
    start_state = problem.getStartState()
    #initial state
    actions = [] 
    #list of the actions that the agent took so far to get to its state(position)
    cost = 0
    start_node = (start_state,actions,cost) 
    #node to hold the state and the array of actions
    visited_states = []

    fringe.push(start_node,cost) 

    while not fringe.isEmpty():
 
        current_node = fringe.pop()
        current_state = current_node[0] 
        #current position
        current_actions = current_node [1] 
        #the actions the agent took so far to get to the current position 
        current_cost = current_node[2]

        if (current_state not in visited_states):
            visited_states.append(current_state)

            if (problem.isGoalState(current_state)): 
                #if goal return the list of actions
                return current_actions
            
            else:
                successors = problem.getSuccessors(current_state) 
                #list of successors of the current state

                for successor in successors:
                    successor_state = successor[0] 
                    #successor position
                    successor_action = successor[1] 
                    #successor's required action to get to its position
                    successor_cost = successor[2]
                    #successor's required cost
                    actions = current_actions + [successor_action] 
                    #add the action to the action list
                    next_node = (successor_state,actions,current_cost)
                    fringe.push(next_node,successor_cost)
                    #push the next successor node that contains its state aka position
    return actions
       

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    fringe = util.PriorityQueue() 
    start_state = problem.getStartState()
    #initial state
    actions = [] 
    # list of the actions that the agent took so far to get to its state(position)
    start_cost = 0
    start_heuristic = heuristic(start_state, problem)
    # The heuristic of the the start state
    start_node = (start_state,actions, start_cost)
    #node to hold the state and the array of actions
    visited_states = []

    fringe.push(start_node,start_cost+start_heuristic) 
    #f(n) = g(n) + h(n), passing down the heuristic + cost as priority
    while not fringe.isEmpty():
 
        current_node = fringe.pop()
        #pops the state with the least cost + heuristic 
        current_state = current_node[0]
        #current position
        current_actions = current_node [1] 
        #the actions the agent took so far to get to the current position 
        current_cost = current_node[2]
        #total sum of cost up until our current state

        if (current_state not in visited_states):
            visited_states.append(current_state)

            if (problem.isGoalState(current_state)): 
                #if current state is the goal return its list of actions
                return current_actions
            
            else:
                successors = problem.getSuccessors(current_state) 
                #list of successors of the current state

                for successor in successors:
                    successor_state = successor[0] 
                    #successor position
                    successor_action = successor[1] 
                    #successor's required action to get to its position
                    successor_cost = successor[2]
                    #the cost to pay to get to the successor
                    successor_heuristic = heuristic(successor_state, problem)
                    #successor's heuristic 
                    successor_total_cost = current_cost + successor_cost
                    #total sum of costs up until this successor state
                    actions = current_actions + [successor_action] 
                    #add the action to the action list
                    next_node = (successor_state,actions,successor_total_cost)
                    fringe.push(next_node,successor_total_cost+successor_heuristic)
                    #passing down the total cost and heuristic as a priority
   
    return actions



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
