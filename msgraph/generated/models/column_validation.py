from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import display_name_localization

class ColumnValidation(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new columnValidation and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Default BCP 47 language tag for the description.
        self._default_language: Optional[str] = None
        # Localized messages that explain what is needed for this column's value to be considered valid. User will be prompted with this message if validation fails.
        self._descriptions: Optional[List[display_name_localization.DisplayNameLocalization]] = None
        # The formula to validate column value. For examples, see Examples of common formulas in lists
        self._formula: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ColumnValidation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ColumnValidation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ColumnValidation()
    
    @property
    def default_language(self,) -> Optional[str]:
        """
        Gets the defaultLanguage property value. Default BCP 47 language tag for the description.
        Returns: Optional[str]
        """
        return self._default_language
    
    @default_language.setter
    def default_language(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultLanguage property value. Default BCP 47 language tag for the description.
        Args:
            value: Value to set for the default_language property.
        """
        self._default_language = value
    
    @property
    def descriptions(self,) -> Optional[List[display_name_localization.DisplayNameLocalization]]:
        """
        Gets the descriptions property value. Localized messages that explain what is needed for this column's value to be considered valid. User will be prompted with this message if validation fails.
        Returns: Optional[List[display_name_localization.DisplayNameLocalization]]
        """
        return self._descriptions
    
    @descriptions.setter
    def descriptions(self,value: Optional[List[display_name_localization.DisplayNameLocalization]] = None) -> None:
        """
        Sets the descriptions property value. Localized messages that explain what is needed for this column's value to be considered valid. User will be prompted with this message if validation fails.
        Args:
            value: Value to set for the descriptions property.
        """
        self._descriptions = value
    
    @property
    def formula(self,) -> Optional[str]:
        """
        Gets the formula property value. The formula to validate column value. For examples, see Examples of common formulas in lists
        Returns: Optional[str]
        """
        return self._formula
    
    @formula.setter
    def formula(self,value: Optional[str] = None) -> None:
        """
        Sets the formula property value. The formula to validate column value. For examples, see Examples of common formulas in lists
        Args:
            value: Value to set for the formula property.
        """
        self._formula = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import display_name_localization

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultLanguage": lambda n : setattr(self, 'default_language', n.get_str_value()),
            "descriptions": lambda n : setattr(self, 'descriptions', n.get_collection_of_object_values(display_name_localization.DisplayNameLocalization)),
            "formula": lambda n : setattr(self, 'formula', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
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
            value: Value to set for the odata_type property.
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
        writer.write_str_value("defaultLanguage", self.default_language)
        writer.write_collection_of_object_values("descriptions", self.descriptions)
        writer.write_str_value("formula", self.formula)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

