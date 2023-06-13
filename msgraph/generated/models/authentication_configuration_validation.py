from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import generic_error

@dataclass
class AuthenticationConfigurationValidation(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Errors in the validation result of a customAuthenticationExtension.
    errors: Optional[List[generic_error.GenericError]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Warnings in the validation result of a customAuthenticationExtension.
    warnings: Optional[List[generic_error.GenericError]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationConfigurationValidation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationConfigurationValidation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationConfigurationValidation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import generic_error

        fields: Dict[str, Callable[[Any], None]] = {
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_object_values(generic_error.GenericError)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "warnings": lambda n : setattr(self, 'warnings', n.get_collection_of_object_values(generic_error.GenericError)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("errors", self.errors)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("warnings", self.warnings)
        writer.write_additional_data_value(self.additional_data)
    

