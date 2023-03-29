from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import host_reputation_rule_severity

class HostReputationRule(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new hostReputationRule and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The description of the rule that gives more context.
        self._description: Optional[str] = None
        # The name of the rule.
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Link to a web page with details related to this rule.
        self._related_details_url: Optional[str] = None
        # The severity property
        self._severity: Optional[host_reputation_rule_severity.HostReputationRuleSeverity] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HostReputationRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: HostReputationRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return HostReputationRule()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the rule that gives more context.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the rule that gives more context.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import host_reputation_rule_severity

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "relatedDetailsUrl": lambda n : setattr(self, 'related_details_url', n.get_str_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(host_reputation_rule_severity.HostReputationRuleSeverity)),
        }
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name of the rule.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name of the rule.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
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
    
    @property
    def related_details_url(self,) -> Optional[str]:
        """
        Gets the relatedDetailsUrl property value. Link to a web page with details related to this rule.
        Returns: Optional[str]
        """
        return self._related_details_url
    
    @related_details_url.setter
    def related_details_url(self,value: Optional[str] = None) -> None:
        """
        Sets the relatedDetailsUrl property value. Link to a web page with details related to this rule.
        Args:
            value: Value to set for the related_details_url property.
        """
        self._related_details_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("description", self.description)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("relatedDetailsUrl", self.related_details_url)
        writer.write_enum_value("severity", self.severity)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def severity(self,) -> Optional[host_reputation_rule_severity.HostReputationRuleSeverity]:
        """
        Gets the severity property value. The severity property
        Returns: Optional[host_reputation_rule_severity.HostReputationRuleSeverity]
        """
        return self._severity
    
    @severity.setter
    def severity(self,value: Optional[host_reputation_rule_severity.HostReputationRuleSeverity] = None) -> None:
        """
        Sets the severity property value. The severity property
        Args:
            value: Value to set for the severity property.
        """
        self._severity = value
    

