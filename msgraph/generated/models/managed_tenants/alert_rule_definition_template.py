from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alert_severity

class AlertRuleDefinitionTemplate(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new alertRuleDefinitionTemplate and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The defaultSeverity property
        self._default_severity: Optional[alert_severity.AlertSeverity] = None
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AlertRuleDefinitionTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AlertRuleDefinitionTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AlertRuleDefinitionTemplate()
    
    @property
    def default_severity(self,) -> Optional[alert_severity.AlertSeverity]:
        """
        Gets the defaultSeverity property value. The defaultSeverity property
        Returns: Optional[alert_severity.AlertSeverity]
        """
        return self._default_severity
    
    @default_severity.setter
    def default_severity(self,value: Optional[alert_severity.AlertSeverity] = None) -> None:
        """
        Sets the defaultSeverity property value. The defaultSeverity property
        Args:
            value: Value to set for the default_severity property.
        """
        self._default_severity = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import alert_severity

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultSeverity": lambda n : setattr(self, 'default_severity', n.get_enum_value(alert_severity.AlertSeverity)),
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
        writer.write_enum_value("defaultSeverity", self.default_severity)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

