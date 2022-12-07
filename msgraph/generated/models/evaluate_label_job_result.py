from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

matching_label = lazy_import('msgraph.generated.models.matching_label')
responsible_policy = lazy_import('msgraph.generated.models.responsible_policy')
responsible_sensitive_type = lazy_import('msgraph.generated.models.responsible_sensitive_type')

class EvaluateLabelJobResult(AdditionalDataHolder, Parsable):
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
        Instantiates a new evaluateLabelJobResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The responsiblePolicy property
        self._responsible_policy: Optional[responsible_policy.ResponsiblePolicy] = None
        # The responsibleSensitiveTypes property
        self._responsible_sensitive_types: Optional[List[responsible_sensitive_type.ResponsibleSensitiveType]] = None
        # The sensitivityLabel property
        self._sensitivity_label: Optional[matching_label.MatchingLabel] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EvaluateLabelJobResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EvaluateLabelJobResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EvaluateLabelJobResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "responsible_policy": lambda n : setattr(self, 'responsible_policy', n.get_object_value(responsible_policy.ResponsiblePolicy)),
            "responsible_sensitive_types": lambda n : setattr(self, 'responsible_sensitive_types', n.get_collection_of_object_values(responsible_sensitive_type.ResponsibleSensitiveType)),
            "sensitivity_label": lambda n : setattr(self, 'sensitivity_label', n.get_object_value(matching_label.MatchingLabel)),
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
    
    @property
    def responsible_policy(self,) -> Optional[responsible_policy.ResponsiblePolicy]:
        """
        Gets the responsiblePolicy property value. The responsiblePolicy property
        Returns: Optional[responsible_policy.ResponsiblePolicy]
        """
        return self._responsible_policy
    
    @responsible_policy.setter
    def responsible_policy(self,value: Optional[responsible_policy.ResponsiblePolicy] = None) -> None:
        """
        Sets the responsiblePolicy property value. The responsiblePolicy property
        Args:
            value: Value to set for the responsiblePolicy property.
        """
        self._responsible_policy = value
    
    @property
    def responsible_sensitive_types(self,) -> Optional[List[responsible_sensitive_type.ResponsibleSensitiveType]]:
        """
        Gets the responsibleSensitiveTypes property value. The responsibleSensitiveTypes property
        Returns: Optional[List[responsible_sensitive_type.ResponsibleSensitiveType]]
        """
        return self._responsible_sensitive_types
    
    @responsible_sensitive_types.setter
    def responsible_sensitive_types(self,value: Optional[List[responsible_sensitive_type.ResponsibleSensitiveType]] = None) -> None:
        """
        Sets the responsibleSensitiveTypes property value. The responsibleSensitiveTypes property
        Args:
            value: Value to set for the responsibleSensitiveTypes property.
        """
        self._responsible_sensitive_types = value
    
    @property
    def sensitivity_label(self,) -> Optional[matching_label.MatchingLabel]:
        """
        Gets the sensitivityLabel property value. The sensitivityLabel property
        Returns: Optional[matching_label.MatchingLabel]
        """
        return self._sensitivity_label
    
    @sensitivity_label.setter
    def sensitivity_label(self,value: Optional[matching_label.MatchingLabel] = None) -> None:
        """
        Sets the sensitivityLabel property value. The sensitivityLabel property
        Args:
            value: Value to set for the sensitivityLabel property.
        """
        self._sensitivity_label = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("responsiblePolicy", self.responsible_policy)
        writer.write_collection_of_object_values("responsibleSensitiveTypes", self.responsible_sensitive_types)
        writer.write_object_value("sensitivityLabel", self.sensitivity_label)
        writer.write_additional_data_value(self.additional_data)
    

