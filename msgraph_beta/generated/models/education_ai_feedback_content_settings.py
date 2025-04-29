from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class EducationAiFeedbackContentSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The isMessageClarityEnabled property
    is_message_clarity_enabled: Optional[bool] = None
    # The isQualityOfInformationEnabled property
    is_quality_of_information_enabled: Optional[bool] = None
    # The isSpeechOrganizationEnabled property
    is_speech_organization_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationAiFeedbackContentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationAiFeedbackContentSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationAiFeedbackContentSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "isMessageClarityEnabled": lambda n : setattr(self, 'is_message_clarity_enabled', n.get_bool_value()),
            "isQualityOfInformationEnabled": lambda n : setattr(self, 'is_quality_of_information_enabled', n.get_bool_value()),
            "isSpeechOrganizationEnabled": lambda n : setattr(self, 'is_speech_organization_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_bool_value("isMessageClarityEnabled", self.is_message_clarity_enabled)
        writer.write_bool_value("isQualityOfInformationEnabled", self.is_quality_of_information_enabled)
        writer.write_bool_value("isSpeechOrganizationEnabled", self.is_speech_organization_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

