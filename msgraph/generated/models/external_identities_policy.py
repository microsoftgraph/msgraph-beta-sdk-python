from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

policy_base = lazy_import('msgraph.generated.models.policy_base')

class ExternalIdentitiesPolicy(policy_base.PolicyBase):
    @property
    def allow_deleted_identities_data_removal(self,) -> Optional[bool]:
        """
        Gets the allowDeletedIdentitiesDataRemoval property value. Reserved for future use.
        Returns: Optional[bool]
        """
        return self._allow_deleted_identities_data_removal
    
    @allow_deleted_identities_data_removal.setter
    def allow_deleted_identities_data_removal(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowDeletedIdentitiesDataRemoval property value. Reserved for future use.
        Args:
            value: Value to set for the allowDeletedIdentitiesDataRemoval property.
        """
        self._allow_deleted_identities_data_removal = value
    
    @property
    def allow_external_identities_to_leave(self,) -> Optional[bool]:
        """
        Gets the allowExternalIdentitiesToLeave property value. Defines whether external users can leave the guest tenant. If set to false, self-service controls are disabled, and the admin of the guest tenant must manually remove the external user from the guest tenant. When the external user leaves the tenant, their data in the guest tenant is first soft-deleted then permanently deleted in 30 days.
        Returns: Optional[bool]
        """
        return self._allow_external_identities_to_leave
    
    @allow_external_identities_to_leave.setter
    def allow_external_identities_to_leave(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowExternalIdentitiesToLeave property value. Defines whether external users can leave the guest tenant. If set to false, self-service controls are disabled, and the admin of the guest tenant must manually remove the external user from the guest tenant. When the external user leaves the tenant, their data in the guest tenant is first soft-deleted then permanently deleted in 30 days.
        Args:
            value: Value to set for the allowExternalIdentitiesToLeave property.
        """
        self._allow_external_identities_to_leave = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ExternalIdentitiesPolicy and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.externalIdentitiesPolicy"
        # Reserved for future use.
        self._allow_deleted_identities_data_removal: Optional[bool] = None
        # Defines whether external users can leave the guest tenant. If set to false, self-service controls are disabled, and the admin of the guest tenant must manually remove the external user from the guest tenant. When the external user leaves the tenant, their data in the guest tenant is first soft-deleted then permanently deleted in 30 days.
        self._allow_external_identities_to_leave: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExternalIdentitiesPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExternalIdentitiesPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExternalIdentitiesPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_deleted_identities_data_removal": lambda n : setattr(self, 'allow_deleted_identities_data_removal', n.get_bool_value()),
            "allow_external_identities_to_leave": lambda n : setattr(self, 'allow_external_identities_to_leave', n.get_bool_value()),
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
        writer.write_bool_value("allowDeletedIdentitiesDataRemoval", self.allow_deleted_identities_data_removal)
        writer.write_bool_value("allowExternalIdentitiesToLeave", self.allow_external_identities_to_leave)
    

