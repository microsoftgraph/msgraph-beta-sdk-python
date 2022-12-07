from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

action_url = lazy_import('msgraph.generated.models.action_url')

class ActionStep(AdditionalDataHolder, Parsable):
    @property
    def action_url(self,) -> Optional[action_url.ActionUrl]:
        """
        Gets the actionUrl property value. The actionUrl property
        Returns: Optional[action_url.ActionUrl]
        """
        return self._action_url
    
    @action_url.setter
    def action_url(self,value: Optional[action_url.ActionUrl] = None) -> None:
        """
        Sets the actionUrl property value. The actionUrl property
        Args:
            value: Value to set for the actionUrl property.
        """
        self._action_url = value
    
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
        Instantiates a new actionStep and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The actionUrl property
        self._action_url: Optional[action_url.ActionUrl] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The stepNumber property
        self._step_number: Optional[int] = None
        # The text property
        self._text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ActionStep:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ActionStep
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ActionStep()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action_url": lambda n : setattr(self, 'action_url', n.get_object_value(action_url.ActionUrl)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "step_number": lambda n : setattr(self, 'step_number', n.get_int_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
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
        writer.write_object_value("actionUrl", self.action_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("stepNumber", self.step_number)
        writer.write_str_value("text", self.text)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def step_number(self,) -> Optional[int]:
        """
        Gets the stepNumber property value. The stepNumber property
        Returns: Optional[int]
        """
        return self._step_number
    
    @step_number.setter
    def step_number(self,value: Optional[int] = None) -> None:
        """
        Sets the stepNumber property value. The stepNumber property
        Args:
            value: Value to set for the stepNumber property.
        """
        self._step_number = value
    
    @property
    def text(self,) -> Optional[str]:
        """
        Gets the text property value. The text property
        Returns: Optional[str]
        """
        return self._text
    
    @text.setter
    def text(self,value: Optional[str] = None) -> None:
        """
        Sets the text property value. The text property
        Args:
            value: Value to set for the text property.
        """
        self._text = value
    

