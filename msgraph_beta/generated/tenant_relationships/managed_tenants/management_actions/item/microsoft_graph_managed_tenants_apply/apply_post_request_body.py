from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ApplyPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The excludeGroups property
    exclude_groups: Optional[List[str]] = None
    # The includeAllUsers property
    include_all_users: Optional[bool] = None
    # The includeGroups property
    include_groups: Optional[List[str]] = None
    # The managementTemplateId property
    management_template_id: Optional[str] = None
    # The tenantGroupId property
    tenant_group_id: Optional[str] = None
    # The tenantId property
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApplyPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplyPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApplyPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "excludeGroups": lambda n : setattr(self, 'exclude_groups', n.get_collection_of_primitive_values(str)),
            "includeAllUsers": lambda n : setattr(self, 'include_all_users', n.get_bool_value()),
            "includeGroups": lambda n : setattr(self, 'include_groups', n.get_collection_of_primitive_values(str)),
            "managementTemplateId": lambda n : setattr(self, 'management_template_id', n.get_str_value()),
            "tenantGroupId": lambda n : setattr(self, 'tenant_group_id', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("excludeGroups", self.exclude_groups)
        writer.write_bool_value("includeAllUsers", self.include_all_users)
        writer.write_collection_of_primitive_values("includeGroups", self.include_groups)
        writer.write_str_value("managementTemplateId", self.management_template_id)
        writer.write_str_value("tenantGroupId", self.tenant_group_id)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_additional_data_value(self.additional_data)
    

