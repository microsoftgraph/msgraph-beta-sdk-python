from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delegated_privilege_status import DelegatedPrivilegeStatus
    from .role_definition import RoleDefinition

@dataclass
class RoleAssignment(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The type of the admin relationship(s) associated with the role assignment. Possible values are: none, delegatedAdminPrivileges, unknownFutureValue, granularDelegatedAdminPrivileges, delegatedAndGranularDelegetedAdminPrivileges. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: granularDelegatedAdminPrivileges , delegatedAndGranularDelegetedAdminPrivileges.
    assignment_type: Optional[DelegatedPrivilegeStatus] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The collection of roles assigned.
    roles: Optional[List[RoleDefinition]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RoleAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RoleAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RoleAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .delegated_privilege_status import DelegatedPrivilegeStatus
        from .role_definition import RoleDefinition

        from .delegated_privilege_status import DelegatedPrivilegeStatus
        from .role_definition import RoleDefinition

        fields: Dict[str, Callable[[Any], None]] = {
            "assignmentType": lambda n : setattr(self, 'assignment_type', n.get_enum_value(DelegatedPrivilegeStatus)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_object_values(RoleDefinition)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("assignmentType", self.assignment_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("roles", self.roles)
        writer.write_additional_data_value(self.additional_data)
    

