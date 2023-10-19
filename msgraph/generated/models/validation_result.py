from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ValidationResult(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The string containing the reason for why the rule passed or not. Read-only. Not nullable.
    message: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The string containing the name of the password validation rule that the action was validated against. Read-only. Not nullable.
    rule_name: Optional[str] = None
    # Whether the password passed or failed the validation rule. Read-only. Not nullable.
    validation_passed: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ValidationResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ValidationResult
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ValidationResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "ruleName": lambda n : setattr(self, 'rule_name', n.get_str_value()),
            "validationPassed": lambda n : setattr(self, 'validation_passed', n.get_bool_value()),
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
        writer.write_str_value("message", self.message)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("ruleName", self.rule_name)
        writer.write_bool_value("validationPassed", self.validation_passed)
        writer.write_additional_data_value(self.additional_data)
    

