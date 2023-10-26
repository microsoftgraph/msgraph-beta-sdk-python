from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policy_scope import PolicyScope

@dataclass
class AzureAdJoinPolicy(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The identifiers of the groups that are in the scope of the policy. Required when the appliesTo property is set to selected.
    allowed_groups: Optional[List[str]] = None
    # The identifiers of users that are in the scope of the policy. Required when the appliesTo property is set to selected.
    allowed_users: Optional[List[str]] = None
    # Specifies whether to block or allow fine-grained control of the policy scope. The possible values are: 0 (meaning none), 1 (meaning all), 2 (meaning selected), 3 (meaning unknownFutureValue). The default value is 1. When set to 2, at least one user or group identifier must be specified in either allowedUsers or allowedGroups.  Setting this property to 0 or 1 removes all identifiers in both allowedUsers and allowedGroups.
    applies_to: Optional[PolicyScope] = None
    # Specifies whether this policy scope is configurable by the admin. The default value is false. When an admin has enabled Intune (MEM) to manage devices, this property is set to false and appliesTo defaults to 1 (meaning all).
    is_admin_configurable: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AzureAdJoinPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AzureAdJoinPolicy
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AzureAdJoinPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .policy_scope import PolicyScope

        from .policy_scope import PolicyScope

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedGroups": lambda n : setattr(self, 'allowed_groups', n.get_collection_of_primitive_values(str)),
            "allowedUsers": lambda n : setattr(self, 'allowed_users', n.get_collection_of_primitive_values(str)),
            "appliesTo": lambda n : setattr(self, 'applies_to', n.get_enum_value(PolicyScope)),
            "isAdminConfigurable": lambda n : setattr(self, 'is_admin_configurable', n.get_bool_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_primitive_values("allowedGroups", self.allowed_groups)
        writer.write_collection_of_primitive_values("allowedUsers", self.allowed_users)
        writer.write_enum_value("appliesTo", self.applies_to)
        writer.write_bool_value("isAdminConfigurable", self.is_admin_configurable)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

