# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
n = Directions.NORTH
s = Directions.SOUTH
e = Directions.EAST
w = Directions.WEST


class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).

  You do not need to change anything in this class, ever.
  """

  def getStartState(self):
     """
     Returns the start state for the search problem
     """
     util.raiseNotDefined()

  def isGoalState(self, state):
     """
       state: Search state

     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state

     For a given state, this should return a list of triples,
     (successor, action, stepCost), where 'successor' is a
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take

     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()


def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  return  [s,s,w,s,w,w,n,s,w]
  
def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def genericSearch(problem, frontiera, euristica=nullHeuristic):
  esplorati = []
  frontiera.push((problem.getStartState(), [] , 0), 0)
  
  while(not(frontiera.isEmpty())):
    stato, azioni, costo = frontiera.pop()
    
    if problem.isGoalState(stato):
      return azioni #soluzione corrispondente
    
    esplorati.append(stato)
    successori = problem.getSuccessors(stato)
    
    for statoSuccessore, azioneSuccessore, costoSuccessore in successori:
      nuovaAzione = azioni + [azioneSuccessore]
      nuovoCosto = costo + costoSuccessore #g(n)
      nodoSuccessore = (statoSuccessore, nuovaAzione, nuovoCosto)
      if statoSuccessore not in esplorati and not frontiera.contains(statoSuccessore, nuovoCosto):
        frontiera.push(nodoSuccessore, nuovoCosto + euristica(statoSuccessore, problem))
        
  return None

def depthFirstSearch(problem):
  "Search the deepest nodes in the search tree first."
  frontiera = util.Stack()
  return genericSearch(problem, frontiera)

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first."
  frontiera = util.Queue()
  return genericSearch(problem, frontiera)

def uniformCostSearch(problem):
  "Search the node of least total cost first."
  frontiera = util.PriorityQueue()
  return genericSearch(problem, frontiera)

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  frontiera = util.PriorityQueue()
  return genericSearch(problem, frontiera, heuristic)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
