from typing import TypedDict, Dict

from rest_framework import status


class Error:
    code: str
    message: str
    http_status_code: int

    def __init__(self, code: str, message: str, http_status_code: int = None):
        self.code = code
        self.message = message
        self.http_status_code = http_status_code


EMAIL_NOT_VERIFIED = "emailNotVerified"
VERIFICATION_TOKEN_INVALID = "verificationTokenInvalid"
USER_BY_TOKEN_MISSING = 'userNOtFoundByToken'
USER_PASS_INVALID = "userPasswordInvalid"
STRIPE_SIGNATURE_FAILED = "stripeSignatureFailed"
LOGIN_IS_BLOCKED = "loginIsBlocked"
ACCOUNT_DISABLED = "accountDisabled"
INVALID_CREDENTIALS = "invalidCredentials"
USER_ALREADY_HAD_COMPANY = "userAlreadyHasCompany"
COMPANY_DOES_NOT_EXISTS = "companyDoesNotExists"
FAVORITE_ALREADY_EXIST = "favoriteAlreadyExist"
FAVORITE_DOES_NOT_EXIST = "favoriteDoesNotExist"
COMPANY_IS_ALREADY_PENDING = "companyIsAlreadyPending"
USER_HAS_NO_ROLE_IN_COMPANY = "userHasNoRoleInCompany"
USER_ALREADY_HAVE_ROLE_IN_COMPANY = "userAlreadyHaveRoleInCompany"
TOKEN_EXPIRED = "tokenExpired"
PRODUCT_DOES_NOT_EXISTS = "productDoesNotExists"
COMPANY_ALREADY_APPROVED = "companyAlreadyApproved"
COMPANY_ALREADY_DISAPPROVED = "companyAlreadyDisapproved"
PRODUCT_ALREADY_PUBLISHED = "productAlreadyPublished"
CATEGORY_DOES_NOT_EXISTS = "categoryDoesNotExists"
CATEGORY_ALREADY_ASSIGNED = "categoryAlreadyAssigned"
CATEGORY_NOT_ALREADY_ASSIGNED = "categoryNotAlreadyAssigned"
FILE_DOES_NOT_EXISTS = "fileDoesNotExists"
PACKAGE_ALREADY_DEACTIVATED = "packageAlreadyDeactivated"
PACKAGE_ALREADY_ACTIVATED = "packageAlreadyActivated"
USER_IS_NOT_IN_COMPANY = "userIsNotInCompany"
PAYMENT_METHOD_MISSING = "paymentMethodMissing"
COMPANY_ALREADY_HAS_SUBSCRIPTION = "companyAlreadyHasSubscription"
PERMISSION_DENIED = "permissionDenied"
USER_IS_ALREADY_ADMIN = "userAlreadyAnAdmin"
USER_IS_NOT_ADMIN = "userIsNotAnAdmin"
COMPANY_HAS_NO_SUBSCRIPTION = "companyHasNoSubscription"
HAVE_NO_ACCESS_TOKEN = "haveNoAccessToken"
LIMIT_REACHED = "limitReached"


ERRORS: Dict[str, Error] = {
    VERIFICATION_TOKEN_INVALID: Error(VERIFICATION_TOKEN_INVALID, "Verification token does not exists",
                                      status.HTTP_400_BAD_REQUEST),
    USER_BY_TOKEN_MISSING: Error(USER_BY_TOKEN_MISSING, "User with provided token does not exist",
                                 status.HTTP_400_BAD_REQUEST),
    EMAIL_NOT_VERIFIED: Error(EMAIL_NOT_VERIFIED, "Email address not verified", status.HTTP_403_FORBIDDEN),
    USER_PASS_INVALID: Error(USER_PASS_INVALID, "User password is not valid.", status.HTTP_400_BAD_REQUEST),
    STRIPE_SIGNATURE_FAILED: Error(STRIPE_SIGNATURE_FAILED, "Stripe webhook signature failed!",
                                   status.HTTP_400_BAD_REQUEST),
    LOGIN_IS_BLOCKED: Error(LOGIN_IS_BLOCKED, "Login is blocked.", status.HTTP_400_BAD_REQUEST),
    INVALID_CREDENTIALS: Error(INVALID_CREDENTIALS, "Invalid credentials.", status.HTTP_400_BAD_REQUEST),
    USER_ALREADY_HAD_COMPANY: Error(
        USER_ALREADY_HAD_COMPANY, "User is already a company owner.", status.HTTP_400_BAD_REQUEST),
    COMPANY_DOES_NOT_EXISTS: Error(
        COMPANY_DOES_NOT_EXISTS, "Company does not exists.", status.HTTP_400_BAD_REQUEST),
    FAVORITE_ALREADY_EXIST: Error(
        FAVORITE_ALREADY_EXIST, "Favorite already exists.", status.HTTP_400_BAD_REQUEST),
    FAVORITE_DOES_NOT_EXIST: Error(
        FAVORITE_DOES_NOT_EXIST, "Favorite does not exists.", status.HTTP_400_BAD_REQUEST),
    COMPANY_IS_ALREADY_PENDING: Error(
        COMPANY_IS_ALREADY_PENDING, "Company is already pending.", status.HTTP_400_BAD_REQUEST),
    USER_HAS_NO_ROLE_IN_COMPANY: Error(
        USER_HAS_NO_ROLE_IN_COMPANY, "User has no role in company.", status.HTTP_400_BAD_REQUEST),
    USER_ALREADY_HAVE_ROLE_IN_COMPANY: Error(
        USER_ALREADY_HAVE_ROLE_IN_COMPANY, "User already have role in company.", status.HTTP_400_BAD_REQUEST),
    TOKEN_EXPIRED: Error(
        TOKEN_EXPIRED, "This token is expired.", status.HTTP_400_BAD_REQUEST),
    PRODUCT_DOES_NOT_EXISTS: Error(
        PRODUCT_DOES_NOT_EXISTS, "Product does not exists.", status.HTTP_400_BAD_REQUEST),
    COMPANY_ALREADY_DISAPPROVED: Error(
        COMPANY_ALREADY_DISAPPROVED, "Company already disapproved", status.HTTP_400_BAD_REQUEST),
    COMPANY_ALREADY_APPROVED: Error(
        COMPANY_ALREADY_APPROVED, "Company already approved", status.HTTP_400_BAD_REQUEST),
    PRODUCT_ALREADY_PUBLISHED: Error(
        PRODUCT_ALREADY_PUBLISHED, "Product is already published", status.HTTP_400_BAD_REQUEST),
    CATEGORY_DOES_NOT_EXISTS: Error(
        CATEGORY_DOES_NOT_EXISTS, "Category does not exists", status.HTTP_400_BAD_REQUEST),
    CATEGORY_ALREADY_ASSIGNED: Error(
        CATEGORY_ALREADY_ASSIGNED, "Category already assigned", status.HTTP_400_BAD_REQUEST),
    CATEGORY_NOT_ALREADY_ASSIGNED: Error(
        CATEGORY_NOT_ALREADY_ASSIGNED, "Category is not assigned", status.HTTP_400_BAD_REQUEST),
    FILE_DOES_NOT_EXISTS: Error(FILE_DOES_NOT_EXISTS, "File does not exists.", status.HTTP_400_BAD_REQUEST),
    PACKAGE_ALREADY_DEACTIVATED: Error(PACKAGE_ALREADY_DEACTIVATED, "Package already deactivated.", status.HTTP_400_BAD_REQUEST),
    PACKAGE_ALREADY_ACTIVATED: Error(PACKAGE_ALREADY_ACTIVATED, "Package already activated.", status.HTTP_400_BAD_REQUEST),
    USER_IS_NOT_IN_COMPANY: Error(USER_IS_NOT_IN_COMPANY, "User is not in company.", status.HTTP_400_BAD_REQUEST),
    PAYMENT_METHOD_MISSING: Error(PAYMENT_METHOD_MISSING, "Payment method missing", status.HTTP_400_BAD_REQUEST),
    COMPANY_ALREADY_HAS_SUBSCRIPTION: Error(
        COMPANY_ALREADY_HAS_SUBSCRIPTION, "Company already has subscription.", status.HTTP_400_BAD_REQUEST),
    PERMISSION_DENIED: Error(PERMISSION_DENIED, "Permission Denied", status.HTTP_403_FORBIDDEN),
    USER_IS_ALREADY_ADMIN: Error(USER_IS_ALREADY_ADMIN, "User is already an admin", status.HTTP_400_BAD_REQUEST),
    USER_IS_NOT_ADMIN: Error(USER_IS_NOT_ADMIN, "User is not an admin", status.HTTP_400_BAD_REQUEST),
    COMPANY_HAS_NO_SUBSCRIPTION: Error(COMPANY_HAS_NO_SUBSCRIPTION, "Company has no subscription", status.HTTP_400_BAD_REQUEST),
    HAVE_NO_ACCESS_TOKEN: Error(HAVE_NO_ACCESS_TOKEN, "User doest not have any access tokens.", status.HTTP_400_BAD_REQUEST),
    LIMIT_REACHED: Error(LIMIT_REACHED, "Limit has reached.", status.HTTP_400_BAD_REQUEST),
}
