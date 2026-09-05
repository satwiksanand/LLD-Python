from enum import Enum

# below are the two examples of enums


## AI Agent state machine
# You are building a backend orchestrator for an autonomous AI agent.
# The agent processes complex tasks, but it can get rate-limited, require human intervention, or fail entirely.
# You need a robust way to track and validate the lifecycle of a task to prevent the system from getting into corrupted states.

class InvalidStateTransitionException(Exception):
    pass

class AgentState(Enum):
    QUEUED = "The task is queued at the moment"
    PROCESSING = "The task is being processed at the moment"
    AWAITING_HUMAN_INTERVENTION = "Human Intervention is required for this task"
    COMPLETED = "The Task has been completed"
    FAILED = "The task has resulted in a failure"

    def __init__(self, message: str):
        self._state_message = message

    @property
    def state_message(self):
        return self._state_message

    def is_terminal(self):
        return self in (AgentState.COMPLETED, AgentState.FAILED)


class StateTransition:
    _allowed_state_transition = {
        AgentState.QUEUED: [AgentState.PROCESSING, AgentState.FAILED],
        AgentState.PROCESSING: [AgentState.AWAITING_HUMAN_INTERVENTION, AgentState.COMPLETED, AgentState.FAILED],
        AgentState.AWAITING_HUMAN_INTERVENTION: [AgentState.PROCESSING, AgentState.FAILED]
    }

    @staticmethod
    def can_transition_to(current_state: AgentState, next_state: AgentState):
        if current_state in StateTransition._allowed_state_transition and next_state in StateTransition._allowed_state_transition[current_state]:
            return True
        return False

class AIAgentStateMachine:
    def __init__(self):
        self._state: AgentState = AgentState.QUEUED  # all the task are initially in the queued state
    # this class is orchestrating the AI agent states and only the valid state transitions are possible

    def print_message(self):
        print(self._state.state_message)

    def transition_to(self, next_state: AgentState):
        if StateTransition.can_transition_to(self._state, next_state):
            self._state = next_state
        else:
            raise InvalidStateTransitionException

if __name__ == "__main__":
    # this will throw an error since there is an invalid transition.
    machine = AIAgentStateMachine()
    machine.print_message()
    machine.transition_to(AgentState.PROCESSING)
    machine.print_message()
    machine.transition_to(AgentState.QUEUED)
    machine.print_message()
    machine.transition_to(AgentState.COMPLETED)
    machine.print_message()