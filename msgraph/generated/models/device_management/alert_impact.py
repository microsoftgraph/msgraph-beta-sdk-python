from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

aggregation_type = lazy_import('msgraph.generated.models.device_management.aggregation_type')

class AlertImpact(AdditionalDataHolder, Parsable):
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
    
    @property
    def aggregation_type(self,) -> Optional[aggregation_type.AggregationType]:
        """
        Gets the aggregationType property value. The aggregation type of the impact. The possible values are: count, percentage, affectedCloudPcCount, affectedCloudPcPercentage, unknownFutureValue.
        Returns: Optional[aggregation_type.AggregationType]
        """
        return self._aggregation_type
    
    @aggregation_type.setter
    def aggregation_type(self,value: Optional[aggregation_type.AggregationType] = None) -> None:
        """
        Sets the aggregationType property value. The aggregation type of the impact. The possible values are: count, percentage, affectedCloudPcCount, affectedCloudPcPercentage, unknownFutureValue.
        Args:
            value: Value to set for the aggregationType property.
        """
        self._aggregation_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new alertImpact and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The aggregation type of the impact. The possible values are: count, percentage, affectedCloudPcCount, affectedCloudPcPercentage, unknownFutureValue.
        self._aggregation_type: Optional[aggregation_type.AggregationType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The number value of the impact.
        self._value: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AlertImpact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AlertImpact
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AlertImpact()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "aggregation_type": lambda n : setattr(self, 'aggregation_type', n.get_enum_value(aggregation_type.AggregationType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_int_value()),
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
        writer.write_enum_value("aggregationType", self.aggregation_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def value(self,) -> Optional[int]:
        """
        Gets the value property value. The number value of the impact.
        Returns: Optional[int]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[int] = None) -> None:
        """
        Sets the value property value. The number value of the impact.
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

