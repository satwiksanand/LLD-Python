# Task: fix the stale minimum-length bug and split responsibilities (Single Responsibility).
# - Validation policy: owns the configurable minimum name length and the email rule.
# - Member registry: owns the set of registered names and duplicate checks.
# - Audit log: owns the "<name>: <result>" entries, one per attempt.
# - MemberSignup keeps its public API and only coordinates these collaborators.
# Rule order stays NAME_TOO_SHORT, INVALID_EMAIL, DUPLICATE, REGISTERED. Changing the
# minimum must affect every future signUp call.

# class MemberSignup:
#     def __init__(self):
#         self._members = set()
#         self._audit = []
#         self._minimum_name_length = 3
#
#     def signUp(self, name: str, email: str) -> str:
#         if len(name) < 3:
#             result = "NAME_TOO_SHORT"
#         else:
#             at = email.find("@")
#             if at <= 0 or at >= len(email) - 1:
#                 result = "INVALID_EMAIL"
#             elif name in self._members:
#                 result = "DUPLICATE"
#             else:
#                 self._members.add(name)
#                 result = "REGISTERED"
#         self._audit.append(f"{name}: {result}")
#         return result
#
#     def setMinimumNameLength(self, minimum: int) -> bool:
#         if minimum < 1 or minimum > 10:
#             return False
#         self._minimum_name_length = minimum
#         return True
#
#     def memberCount(self) -> int:
#         return len(self._members)
#
#     def auditTrail(self) -> list[str]:
#         return list(self._audit)

class ValidationPolicy:
    def __init__(self):
        self._min_length = 3

    def verify_email(self, email: str) -> bool:
        at = email.find("@")
        return 0 < at < len(email) - 1

    def set_minimum_name_length(self, minimum: int) -> bool:
        if minimum < 1 or minimum > 10:
            return False
        self._min_length = minimum
        return True

    def verify_name_length(self, name: str):
        return len(name) >= self._min_length

    def min_length(self):
        return self._min_length

class MemberRegistry:
    def __init__(self):
        self._members = set()

    def member_count(self):
        return len(self._members)

    def add_member(self, name: str):
        if name in self._members:
            return False
        self._members.add(name)
        return True

class AuditLog:
    def __init__(self):
        self._audit = []

    def add_audit(self, name: str, result: str):
        self._audit.append(f"{name}: {result}")

    def audit_trail(self) -> list:
        return list(self._audit)

class MemberSignup:
    def __init__(self):
        self.validation_policy = ValidationPolicy()
        self.member_registry = MemberRegistry()
        self.audit_log = AuditLog()

    def auditTrail(self) -> list[str]:
        return list(self.audit_log.audit_trail())

    def memberCount(self) -> int:
        return self.member_registry.member_count()

    def setMinimumNameLength(self, minimum: int) -> bool:
        return self.validation_policy.set_minimum_name_length(minimum)

    def signUp(self, name: str, email: str) -> str:
        if len(name) < self.validation_policy.min_length():
            result = "NAME_TOO_SHORT"
        else:
            if self.validation_policy.verify_email(email):
                result = "INVALID_EMAIL"
            elif not self.member_registry.add_member(name):
                result = "DUPLICATE"
            else:
                result = "REGISTERED"
        self.audit_log.add_audit(name, result)
        return result