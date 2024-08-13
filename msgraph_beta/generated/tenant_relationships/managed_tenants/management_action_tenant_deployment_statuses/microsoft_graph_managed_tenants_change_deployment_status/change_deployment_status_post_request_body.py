from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ChangeDeploymentStatusPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The managementActionId property
    management_action_id: Optional[str] = None
    # The managementTemplateId property
    management_template_id: Optional[str] = None
    # The managementTemplateVersion property
    management_template_version: Optional[int] = None
    # The status property
    status: Optional[str] = None
    # The tenantGroupId property
    tenant_group_id: Optional[str] = None
    # The tenantId property
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChangeDeploymentStatusPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChangeDeploymentStatusPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChangeDeploymentStatusPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "managementActionId": lambda n : setattr(self, 'management_action_id', n.get_str_value()),
            "managementTemplateId": lambda n : setattr(self, 'management_template_id', n.get_str_value()),
            "managementTemplateVersion": lambda n : setattr(self, 'management_template_version', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_str_value("managementActionId", self.management_action_id)
        writer.write_str_value("managementTemplateId", self.management_template_id)
        writer.write_int_value("managementTemplateVersion", self.management_template_version)
        writer.write_str_value("status", self.status)
        writer.write_str_value("tenantGroupId", self.tenant_group_id)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_additional_data_value(self.additional_data)
    

