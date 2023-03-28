from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import business_scenario

class SolutionsRoot(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new SolutionsRoot and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The businessScenarios property
        self._business_scenarios: Optional[List[business_scenario.BusinessScenario]] = None
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
    
    @property
    def business_scenarios(self,) -> Optional[List[business_scenario.BusinessScenario]]:
        """
        Gets the businessScenarios property value. The businessScenarios property
        Returns: Optional[List[business_scenario.BusinessScenario]]
        """
        return self._business_scenarios
    
    @business_scenarios.setter
    def business_scenarios(self,value: Optional[List[business_scenario.BusinessScenario]] = None) -> None:
        """
        Sets the businessScenarios property value. The businessScenarios property
        Args:
            value: Value to set for the business_scenarios property.
        """
        self._business_scenarios = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SolutionsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SolutionsRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SolutionsRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import business_scenario

        fields: Dict[str, Callable[[Any], None]] = {
            "businessScenarios": lambda n : setattr(self, 'business_scenarios', n.get_collection_of_object_values(business_scenario.BusinessScenario)),
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
        writer.write_collection_of_object_values("businessScenarios", self.business_scenarios)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

