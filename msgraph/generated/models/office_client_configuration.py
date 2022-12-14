from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
office_client_checkin_status = lazy_import('msgraph.generated.models.office_client_checkin_status')
office_client_configuration_assignment = lazy_import('msgraph.generated.models.office_client_configuration_assignment')
office_user_checkin_summary = lazy_import('msgraph.generated.models.office_user_checkin_summary')

class OfficeClientConfiguration(entity.Entity):
    @property
    def assignments(self,) -> Optional[List[office_client_configuration_assignment.OfficeClientConfigurationAssignment]]:
        """
        Gets the assignments property value. The list of group assignments for the policy.
        Returns: Optional[List[office_client_configuration_assignment.OfficeClientConfigurationAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[office_client_configuration_assignment.OfficeClientConfigurationAssignment]] = None) -> None:
        """
        Sets the assignments property value. The list of group assignments for the policy.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    @property
    def checkin_statuses(self,) -> Optional[List[office_client_checkin_status.OfficeClientCheckinStatus]]:
        """
        Gets the checkinStatuses property value. List of office Client check-in status.
        Returns: Optional[List[office_client_checkin_status.OfficeClientCheckinStatus]]
        """
        return self._checkin_statuses
    
    @checkin_statuses.setter
    def checkin_statuses(self,value: Optional[List[office_client_checkin_status.OfficeClientCheckinStatus]] = None) -> None:
        """
        Sets the checkinStatuses property value. List of office Client check-in status.
        Args:
            value: Value to set for the checkinStatuses property.
        """
        self._checkin_statuses = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new OfficeClientConfiguration and sets the default values.
        """
        super().__init__()
        # The list of group assignments for the policy.
        self._assignments: Optional[List[office_client_configuration_assignment.OfficeClientConfigurationAssignment]] = None
        # List of office Client check-in status.
        self._checkin_statuses: Optional[List[office_client_checkin_status.OfficeClientCheckinStatus]] = None
        # Not yet documented
        self._description: Optional[str] = None
        # Admin provided description of the office client configuration policy.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Policy settings JSON string in binary format, these values cannot be changed by the user.
        self._policy_payload: Optional[bytes] = None
        # Priority value should be unique value for each policy under a tenant and will be used for conflict resolution, lower values mean priority is high.
        self._priority: Optional[int] = None
        # User check-in summary for the policy.
        self._user_checkin_summary: Optional[office_user_checkin_summary.OfficeUserCheckinSummary] = None
        # Preference settings JSON string in binary format, these values can be overridden by the user.
        self._user_preference_payload: Optional[bytes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OfficeClientConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OfficeClientConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OfficeClientConfiguration()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Not yet documented
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Not yet documented
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Admin provided description of the office client configuration policy.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Admin provided description of the office client configuration policy.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(office_client_configuration_assignment.OfficeClientConfigurationAssignment)),
            "checkin_statuses": lambda n : setattr(self, 'checkin_statuses', n.get_collection_of_object_values(office_client_checkin_status.OfficeClientCheckinStatus)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "policy_payload": lambda n : setattr(self, 'policy_payload', n.get_bytes_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "user_checkin_summary": lambda n : setattr(self, 'user_checkin_summary', n.get_object_value(office_user_checkin_summary.OfficeUserCheckinSummary)),
            "user_preference_payload": lambda n : setattr(self, 'user_preference_payload', n.get_bytes_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def policy_payload(self,) -> Optional[bytes]:
        """
        Gets the policyPayload property value. Policy settings JSON string in binary format, these values cannot be changed by the user.
        Returns: Optional[bytes]
        """
        return self._policy_payload
    
    @policy_payload.setter
    def policy_payload(self,value: Optional[bytes] = None) -> None:
        """
        Sets the policyPayload property value. Policy settings JSON string in binary format, these values cannot be changed by the user.
        Args:
            value: Value to set for the policyPayload property.
        """
        self._policy_payload = value
    
    @property
    def priority(self,) -> Optional[int]:
        """
        Gets the priority property value. Priority value should be unique value for each policy under a tenant and will be used for conflict resolution, lower values mean priority is high.
        Returns: Optional[int]
        """
        return self._priority
    
    @priority.setter
    def priority(self,value: Optional[int] = None) -> None:
        """
        Sets the priority property value. Priority value should be unique value for each policy under a tenant and will be used for conflict resolution, lower values mean priority is high.
        Args:
            value: Value to set for the priority property.
        """
        self._priority = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_collection_of_object_values("checkinStatuses", self.checkin_statuses)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("policyPayload", self.policy_payload)
        writer.write_int_value("priority", self.priority)
        writer.write_object_value("userCheckinSummary", self.user_checkin_summary)
        writer.write_object_value("userPreferencePayload", self.user_preference_payload)
    
    @property
    def user_checkin_summary(self,) -> Optional[office_user_checkin_summary.OfficeUserCheckinSummary]:
        """
        Gets the userCheckinSummary property value. User check-in summary for the policy.
        Returns: Optional[office_user_checkin_summary.OfficeUserCheckinSummary]
        """
        return self._user_checkin_summary
    
    @user_checkin_summary.setter
    def user_checkin_summary(self,value: Optional[office_user_checkin_summary.OfficeUserCheckinSummary] = None) -> None:
        """
        Sets the userCheckinSummary property value. User check-in summary for the policy.
        Args:
            value: Value to set for the userCheckinSummary property.
        """
        self._user_checkin_summary = value
    
    @property
    def user_preference_payload(self,) -> Optional[bytes]:
        """
        Gets the userPreferencePayload property value. Preference settings JSON string in binary format, these values can be overridden by the user.
        Returns: Optional[bytes]
        """
        return self._user_preference_payload
    
    @user_preference_payload.setter
    def user_preference_payload(self,value: Optional[bytes] = None) -> None:
        """
        Sets the userPreferencePayload property value. Preference settings JSON string in binary format, these values can be overridden by the user.
        Args:
            value: Value to set for the userPreferencePayload property.
        """
        self._user_preference_payload = value
    

