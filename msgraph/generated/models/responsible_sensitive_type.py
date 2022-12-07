from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ResponsibleSensitiveType(AdditionalDataHolder, Parsable):
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
        Instantiates a new responsibleSensitiveType and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The description property
        self._description: Optional[str] = None
        # The id property
        self._id: Optional[str] = None
        # The name property
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The publisherName property
        self._publisher_name: Optional[str] = None
        # The rulePackageId property
        self._rule_package_id: Optional[str] = None
        # The rulePackageType property
        self._rule_package_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ResponsibleSensitiveType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ResponsibleSensitiveType
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ResponsibleSensitiveType()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "publisher_name": lambda n : setattr(self, 'publisher_name', n.get_str_value()),
            "rule_package_id": lambda n : setattr(self, 'rule_package_id', n.get_str_value()),
            "rule_package_type": lambda n : setattr(self, 'rule_package_type', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. The id property
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. The id property
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name property
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name property
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def publisher_name(self,) -> Optional[str]:
        """
        Gets the publisherName property value. The publisherName property
        Returns: Optional[str]
        """
        return self._publisher_name
    
    @publisher_name.setter
    def publisher_name(self,value: Optional[str] = None) -> None:
        """
        Sets the publisherName property value. The publisherName property
        Args:
            value: Value to set for the publisherName property.
        """
        self._publisher_name = value
    
    @property
    def rule_package_id(self,) -> Optional[str]:
        """
        Gets the rulePackageId property value. The rulePackageId property
        Returns: Optional[str]
        """
        return self._rule_package_id
    
    @rule_package_id.setter
    def rule_package_id(self,value: Optional[str] = None) -> None:
        """
        Sets the rulePackageId property value. The rulePackageId property
        Args:
            value: Value to set for the rulePackageId property.
        """
        self._rule_package_id = value
    
    @property
    def rule_package_type(self,) -> Optional[str]:
        """
        Gets the rulePackageType property value. The rulePackageType property
        Returns: Optional[str]
        """
        return self._rule_package_type
    
    @rule_package_type.setter
    def rule_package_type(self,value: Optional[str] = None) -> None:
        """
        Sets the rulePackageType property value. The rulePackageType property
        Args:
            value: Value to set for the rulePackageType property.
        """
        self._rule_package_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("description", self.description)
        writer.write_str_value("id", self.id)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("publisherName", self.publisher_name)
        writer.write_str_value("rulePackageId", self.rule_package_id)
        writer.write_str_value("rulePackageType", self.rule_package_type)
        writer.write_additional_data_value(self.additional_data)
    

