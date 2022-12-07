from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

monitoring_rule = lazy_import('msgraph.generated.models.windows_updates.monitoring_rule')

class MonitoringSettings(AdditionalDataHolder, Parsable):
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
        Instantiates a new monitoringSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Specifies the rules through which monitoring signals can trigger actions on the deployment. Rules are combined using 'or'.
        self._monitoring_rules: Optional[List[monitoring_rule.MonitoringRule]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MonitoringSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MonitoringSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MonitoringSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "monitoring_rules": lambda n : setattr(self, 'monitoring_rules', n.get_collection_of_object_values(monitoring_rule.MonitoringRule)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def monitoring_rules(self,) -> Optional[List[monitoring_rule.MonitoringRule]]:
        """
        Gets the monitoringRules property value. Specifies the rules through which monitoring signals can trigger actions on the deployment. Rules are combined using 'or'.
        Returns: Optional[List[monitoring_rule.MonitoringRule]]
        """
        return self._monitoring_rules
    
    @monitoring_rules.setter
    def monitoring_rules(self,value: Optional[List[monitoring_rule.MonitoringRule]] = None) -> None:
        """
        Sets the monitoringRules property value. Specifies the rules through which monitoring signals can trigger actions on the deployment. Rules are combined using 'or'.
        Args:
            value: Value to set for the monitoringRules property.
        """
        self._monitoring_rules = value
    
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
        writer.write_collection_of_object_values("monitoringRules", self.monitoring_rules)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

