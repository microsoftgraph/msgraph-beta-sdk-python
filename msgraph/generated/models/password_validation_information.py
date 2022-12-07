from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

validation_result = lazy_import('msgraph.generated.models.validation_result')

class PasswordValidationInformation(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new passwordValidationInformation and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Specifies whether the password is valid based on the calculation of the results in the validationResults property. Not nullable. Read-only.
        self._is_valid: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The list of password validation rules and whether the password passed those rules. Not nullable. Read-only.
        self._validation_results: Optional[List[validation_result.ValidationResult]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PasswordValidationInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PasswordValidationInformation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PasswordValidationInformation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_valid": lambda n : setattr(self, 'is_valid', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "validation_results": lambda n : setattr(self, 'validation_results', n.get_collection_of_object_values(validation_result.ValidationResult)),
        }
        return fields
    
    @property
    def is_valid(self,) -> Optional[bool]:
        """
        Gets the isValid property value. Specifies whether the password is valid based on the calculation of the results in the validationResults property. Not nullable. Read-only.
        Returns: Optional[bool]
        """
        return self._is_valid
    
    @is_valid.setter
    def is_valid(self,value: Optional[bool] = None) -> None:
        """
        Sets the isValid property value. Specifies whether the password is valid based on the calculation of the results in the validationResults property. Not nullable. Read-only.
        Args:
            value: Value to set for the isValid property.
        """
        self._is_valid = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("isValid", self.is_valid)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("validationResults", self.validation_results)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def validation_results(self,) -> Optional[List[validation_result.ValidationResult]]:
        """
        Gets the validationResults property value. The list of password validation rules and whether the password passed those rules. Not nullable. Read-only.
        Returns: Optional[List[validation_result.ValidationResult]]
        """
        return self._validation_results
    
    @validation_results.setter
    def validation_results(self,value: Optional[List[validation_result.ValidationResult]] = None) -> None:
        """
        Sets the validationResults property value. The list of password validation rules and whether the password passed those rules. Not nullable. Read-only.
        Args:
            value: Value to set for the validationResults property.
        """
        self._validation_results = value
    

