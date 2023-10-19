from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class BusinessScenarioProperties(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The identifier for the bucketDefinition configured in the plannerPlanConfiguration for the scenario. The task will be placed in the corresponding plannerBucket in the target plan. Required.
    external_bucket_id: Optional[str] = None
    # The identifier for the context of the task. Context is an application controlled value, and tasks can be queried by their externalContextId. Optional.
    external_context_id: Optional[str] = None
    # Application-specific identifier for the task. Every task for the same scenario must have a unique identifier specified for this property. Required.
    external_object_id: Optional[str] = None
    # Application-specific version of the task. Optional.
    external_object_version: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The URL to the application-specific experience for this task. Optional.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BusinessScenarioProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BusinessScenarioProperties
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BusinessScenarioProperties()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "externalBucketId": lambda n : setattr(self, 'external_bucket_id', n.get_str_value()),
            "externalContextId": lambda n : setattr(self, 'external_context_id', n.get_str_value()),
            "externalObjectId": lambda n : setattr(self, 'external_object_id', n.get_str_value()),
            "externalObjectVersion": lambda n : setattr(self, 'external_object_version', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_str_value("externalBucketId", self.external_bucket_id)
        writer.write_str_value("externalContextId", self.external_context_id)
        writer.write_str_value("externalObjectId", self.external_object_id)
        writer.write_str_value("externalObjectVersion", self.external_object_version)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("webUrl", self.web_url)
        writer.write_additional_data_value(self.additional_data)
    

