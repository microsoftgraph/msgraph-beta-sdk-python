from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.key_credential import KeyCredential

@dataclass
class CreateDeviceFromTemplatePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The accountEnabled property
    account_enabled: Optional[bool] = None
    # The alternativeNames property
    alternative_names: Optional[list[str]] = None
    # The externalDeviceId property
    external_device_id: Optional[str] = None
    # The externalSourceName property
    external_source_name: Optional[str] = None
    # The keyCredential property
    key_credential: Optional[KeyCredential] = None
    # The operatingSystemVersion property
    operating_system_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateDeviceFromTemplatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateDeviceFromTemplatePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateDeviceFromTemplatePostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.key_credential import KeyCredential

        from ......models.key_credential import KeyCredential

        fields: dict[str, Callable[[Any], None]] = {
            "accountEnabled": lambda n : setattr(self, 'account_enabled', n.get_bool_value()),
            "alternativeNames": lambda n : setattr(self, 'alternative_names', n.get_collection_of_primitive_values(str)),
            "externalDeviceId": lambda n : setattr(self, 'external_device_id', n.get_str_value()),
            "externalSourceName": lambda n : setattr(self, 'external_source_name', n.get_str_value()),
            "keyCredential": lambda n : setattr(self, 'key_credential', n.get_object_value(KeyCredential)),
            "operatingSystemVersion": lambda n : setattr(self, 'operating_system_version', n.get_str_value()),
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
        writer.write_bool_value("accountEnabled", self.account_enabled)
        writer.write_collection_of_primitive_values("alternativeNames", self.alternative_names)
        writer.write_str_value("externalDeviceId", self.external_device_id)
        writer.write_str_value("externalSourceName", self.external_source_name)
        writer.write_object_value("keyCredential", self.key_credential)
        writer.write_str_value("operatingSystemVersion", self.operating_system_version)
        writer.write_additional_data_value(self.additional_data)
    

