from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import assigned_license, assigned_plan, education_assignment, education_class, education_external_source, education_on_premises_info, education_rubric, education_school, education_student, education_teacher, education_user_role, entity, identity_set, password_profile, physical_address, provisioned_plan, related_contact, user

from . import entity

@dataclass
class EducationUser(entity.Entity):
    # True if the account is enabled; otherwise, false. This property is required when a user is created. Supports /$filter.
    account_enabled: Optional[bool] = None
    # The licenses that are assigned to the user. Not nullable.
    assigned_licenses: Optional[List[assigned_license.AssignedLicense]] = None
    # The plans that are assigned to the user. Read-only. Not nullable.
    assigned_plans: Optional[List[assigned_plan.AssignedPlan]] = None
    # List of assignments for the user. Nullable.
    assignments: Optional[List[education_assignment.EducationAssignment]] = None
    # The telephone numbers for the user. Note: Although this is a string collection, only one number can be set for this property.
    business_phones: Optional[List[str]] = None
    # Classes to which the user belongs. Nullable.
    classes: Optional[List[education_class.EducationClass]] = None
    # Entity who created the user.
    created_by: Optional[identity_set.IdentitySet] = None
    # The name for the department in which the user works. Supports /$filter.
    department: Optional[str] = None
    # The name displayed in the address book for the user. Supports $filter and $orderby.
    display_name: Optional[str] = None
    # The type of external source this resource was generated from (automatically determined from externalSourceDetail). Possible values are: sis, lms, or manual.
    external_source: Optional[education_external_source.EducationExternalSource] = None
    # The name of the external source this resources was generated from.
    external_source_detail: Optional[str] = None
    # The given name (first name) of the user. Supports /$filter.
    given_name: Optional[str] = None
    # The SMTP address for the user; for example, 'jeff@contoso.onmicrosoft.com'. Read-Only. Supports /$filter.
    mail: Optional[str] = None
    # The mail alias for the user. This property must be specified when a user is created. Supports /$filter.
    mail_nickname: Optional[str] = None
    # Mail address of user. Note: type and postOfficeBox are not supported for educationUser resources.
    mailing_address: Optional[physical_address.PhysicalAddress] = None
    # The middle name of user.
    middle_name: Optional[str] = None
    # The primary cellular telephone number for the user.
    mobile_phone: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The officeLocation property
    office_location: Optional[str] = None
    # Additional information used to associate the AAD user with it's Active Directory counterpart.
    on_premises_info: Optional[education_on_premises_info.EducationOnPremisesInfo] = None
    # Specifies password policies for the user. See standard [user] resource for additional details.
    password_policies: Optional[str] = None
    # Specifies the password profile for the user. The profile contains the user's password. This property is required when a user is created. See standard [user] resource for additional details.
    password_profile: Optional[password_profile.PasswordProfile] = None
    # The preferred language for the user. Should follow ISO 639-1 Code; for example, 'en-US'.
    preferred_language: Optional[str] = None
    # The primaryRole property
    primary_role: Optional[education_user_role.EducationUserRole] = None
    # The plans that are provisioned for the user. Read-only. Not nullable.
    provisioned_plans: Optional[List[provisioned_plan.ProvisionedPlan]] = None
    # The refreshTokensValidFromDateTime property
    refresh_tokens_valid_from_date_time: Optional[datetime] = None
    # Related records related to the user. Possible relationships are parent, relative, aide, doctor, guardian, child, other, unknownFutureValue
    related_contacts: Optional[List[related_contact.RelatedContact]] = None
    # Address where user lives. Note: type and postOfficeBox are not supported for educationUser resources.
    residence_address: Optional[physical_address.PhysicalAddress] = None
    # When set, the grading rubric attached to the assignment.
    rubrics: Optional[List[education_rubric.EducationRubric]] = None
    # Schools to which the user belongs. Nullable.
    schools: Optional[List[education_school.EducationSchool]] = None
    # The showInAddressList property
    show_in_address_list: Optional[bool] = None
    # If the primary role is student, this block will contain student specific data.
    student: Optional[education_student.EducationStudent] = None
    # The user's surname (family name or last name). Supports /$filter.
    surname: Optional[str] = None
    # Classes for which the user is a teacher.
    taught_classes: Optional[List[education_class.EducationClass]] = None
    # If the primary role is teacher, this block will contain teacher specific data.
    teacher: Optional[education_teacher.EducationTeacher] = None
    # A two-letter country code ([ISO 3166 Alpha-2]). Required for users who will be assigned licenses. Not nullable. Supports /$filter.
    usage_location: Optional[str] = None
    # The user property
    user: Optional[user.User] = None
    # The user principal name (UPN) for the user. Supports $filter and $orderby. See standard [user] resource for additional details.
    user_principal_name: Optional[str] = None
    # A string value that can be used to classify user types in your directory, such as 'Member' and 'Guest'. Supports /$filter.
    user_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationUser
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EducationUser()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import assigned_license, assigned_plan, education_assignment, education_class, education_external_source, education_on_premises_info, education_rubric, education_school, education_student, education_teacher, education_user_role, entity, identity_set, password_profile, physical_address, provisioned_plan, related_contact, user

        from . import assigned_license, assigned_plan, education_assignment, education_class, education_external_source, education_on_premises_info, education_rubric, education_school, education_student, education_teacher, education_user_role, entity, identity_set, password_profile, physical_address, provisioned_plan, related_contact, user

        fields: Dict[str, Callable[[Any], None]] = {
            "accountEnabled": lambda n : setattr(self, 'account_enabled', n.get_bool_value()),
            "assignedLicenses": lambda n : setattr(self, 'assigned_licenses', n.get_collection_of_object_values(assigned_license.AssignedLicense)),
            "assignedPlans": lambda n : setattr(self, 'assigned_plans', n.get_collection_of_object_values(assigned_plan.AssignedPlan)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(education_assignment.EducationAssignment)),
            "businessPhones": lambda n : setattr(self, 'business_phones', n.get_collection_of_primitive_values(str)),
            "classes": lambda n : setattr(self, 'classes', n.get_collection_of_object_values(education_class.EducationClass)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "department": lambda n : setattr(self, 'department', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "externalSource": lambda n : setattr(self, 'external_source', n.get_enum_value(education_external_source.EducationExternalSource)),
            "externalSourceDetail": lambda n : setattr(self, 'external_source_detail', n.get_str_value()),
            "givenName": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "mail": lambda n : setattr(self, 'mail', n.get_str_value()),
            "mailNickname": lambda n : setattr(self, 'mail_nickname', n.get_str_value()),
            "mailingAddress": lambda n : setattr(self, 'mailing_address', n.get_object_value(physical_address.PhysicalAddress)),
            "middleName": lambda n : setattr(self, 'middle_name', n.get_str_value()),
            "mobilePhone": lambda n : setattr(self, 'mobile_phone', n.get_str_value()),
            "officeLocation": lambda n : setattr(self, 'office_location', n.get_str_value()),
            "onPremisesInfo": lambda n : setattr(self, 'on_premises_info', n.get_object_value(education_on_premises_info.EducationOnPremisesInfo)),
            "passwordPolicies": lambda n : setattr(self, 'password_policies', n.get_str_value()),
            "passwordProfile": lambda n : setattr(self, 'password_profile', n.get_object_value(password_profile.PasswordProfile)),
            "preferredLanguage": lambda n : setattr(self, 'preferred_language', n.get_str_value()),
            "primaryRole": lambda n : setattr(self, 'primary_role', n.get_enum_value(education_user_role.EducationUserRole)),
            "provisionedPlans": lambda n : setattr(self, 'provisioned_plans', n.get_collection_of_object_values(provisioned_plan.ProvisionedPlan)),
            "refreshTokensValidFromDateTime": lambda n : setattr(self, 'refresh_tokens_valid_from_date_time', n.get_datetime_value()),
            "relatedContacts": lambda n : setattr(self, 'related_contacts', n.get_collection_of_object_values(related_contact.RelatedContact)),
            "residenceAddress": lambda n : setattr(self, 'residence_address', n.get_object_value(physical_address.PhysicalAddress)),
            "rubrics": lambda n : setattr(self, 'rubrics', n.get_collection_of_object_values(education_rubric.EducationRubric)),
            "schools": lambda n : setattr(self, 'schools', n.get_collection_of_object_values(education_school.EducationSchool)),
            "showInAddressList": lambda n : setattr(self, 'show_in_address_list', n.get_bool_value()),
            "student": lambda n : setattr(self, 'student', n.get_object_value(education_student.EducationStudent)),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "taughtClasses": lambda n : setattr(self, 'taught_classes', n.get_collection_of_object_values(education_class.EducationClass)),
            "teacher": lambda n : setattr(self, 'teacher', n.get_object_value(education_teacher.EducationTeacher)),
            "usageLocation": lambda n : setattr(self, 'usage_location', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(user.User)),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "userType": lambda n : setattr(self, 'user_type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("accountEnabled", self.account_enabled)
        writer.write_collection_of_object_values("assignedLicenses", self.assigned_licenses)
        writer.write_collection_of_object_values("assignedPlans", self.assigned_plans)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_collection_of_primitive_values("businessPhones", self.business_phones)
        writer.write_collection_of_object_values("classes", self.classes)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_str_value("department", self.department)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("externalSource", self.external_source)
        writer.write_str_value("externalSourceDetail", self.external_source_detail)
        writer.write_str_value("givenName", self.given_name)
        writer.write_str_value("mail", self.mail)
        writer.write_str_value("mailNickname", self.mail_nickname)
        writer.write_object_value("mailingAddress", self.mailing_address)
        writer.write_str_value("middleName", self.middle_name)
        writer.write_str_value("mobilePhone", self.mobile_phone)
        writer.write_str_value("officeLocation", self.office_location)
        writer.write_object_value("onPremisesInfo", self.on_premises_info)
        writer.write_str_value("passwordPolicies", self.password_policies)
        writer.write_object_value("passwordProfile", self.password_profile)
        writer.write_str_value("preferredLanguage", self.preferred_language)
        writer.write_enum_value("primaryRole", self.primary_role)
        writer.write_collection_of_object_values("provisionedPlans", self.provisioned_plans)
        writer.write_datetime_value("refreshTokensValidFromDateTime", self.refresh_tokens_valid_from_date_time)
        writer.write_collection_of_object_values("relatedContacts", self.related_contacts)
        writer.write_object_value("residenceAddress", self.residence_address)
        writer.write_collection_of_object_values("rubrics", self.rubrics)
        writer.write_collection_of_object_values("schools", self.schools)
        writer.write_bool_value("showInAddressList", self.show_in_address_list)
        writer.write_object_value("student", self.student)
        writer.write_str_value("surname", self.surname)
        writer.write_collection_of_object_values("taughtClasses", self.taught_classes)
        writer.write_object_value("teacher", self.teacher)
        writer.write_str_value("usageLocation", self.usage_location)
        writer.write_object_value("user", self.user)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_str_value("userType", self.user_type)
    

