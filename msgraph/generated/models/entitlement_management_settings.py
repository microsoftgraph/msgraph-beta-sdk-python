from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class EntitlementManagementSettings(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new entitlementManagementSettings and sets the default values.
        """
        super().__init__()
        # If externalUserLifecycleAction is BlockSignInAndDelete, the number of days after an external user is blocked from sign in before their account is deleted.
        self._days_until_external_user_deleted_after_blocked: Optional[int] = None
        # One of None, BlockSignIn, or BlockSignInAndDelete.
        self._external_user_lifecycle_action: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EntitlementManagementSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EntitlementManagementSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EntitlementManagementSettings()
    
    @property
    def days_until_external_user_deleted_after_blocked(self,) -> Optional[int]:
        """
        Gets the daysUntilExternalUserDeletedAfterBlocked property value. If externalUserLifecycleAction is BlockSignInAndDelete, the number of days after an external user is blocked from sign in before their account is deleted.
        Returns: Optional[int]
        """
        return self._days_until_external_user_deleted_after_blocked
    
    @days_until_external_user_deleted_after_blocked.setter
    def days_until_external_user_deleted_after_blocked(self,value: Optional[int] = None) -> None:
        """
        Sets the daysUntilExternalUserDeletedAfterBlocked property value. If externalUserLifecycleAction is BlockSignInAndDelete, the number of days after an external user is blocked from sign in before their account is deleted.
        Args:
            value: Value to set for the daysUntilExternalUserDeletedAfterBlocked property.
        """
        self._days_until_external_user_deleted_after_blocked = value
    
    @property
    def external_user_lifecycle_action(self,) -> Optional[str]:
        """
        Gets the externalUserLifecycleAction property value. One of None, BlockSignIn, or BlockSignInAndDelete.
        Returns: Optional[str]
        """
        return self._external_user_lifecycle_action
    
    @external_user_lifecycle_action.setter
    def external_user_lifecycle_action(self,value: Optional[str] = None) -> None:
        """
        Sets the externalUserLifecycleAction property value. One of None, BlockSignIn, or BlockSignInAndDelete.
        Args:
            value: Value to set for the externalUserLifecycleAction property.
        """
        self._external_user_lifecycle_action = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "days_until_external_user_deleted_after_blocked": lambda n : setattr(self, 'days_until_external_user_deleted_after_blocked', n.get_int_value()),
            "external_user_lifecycle_action": lambda n : setattr(self, 'external_user_lifecycle_action', n.get_str_value()),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("daysUntilExternalUserDeletedAfterBlocked", self.days_until_external_user_deleted_after_blocked)
        writer.write_str_value("externalUserLifecycleAction", self.external_user_lifecycle_action)
    

