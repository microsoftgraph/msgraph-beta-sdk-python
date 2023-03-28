from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import classification_method, entity, sensitive_type_scope, sensitive_type_source

from . import entity

class SensitiveType(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new sensitiveType and sets the default values.
        """
        super().__init__()
        # The classificationMethod property
        self._classification_method: Optional[classification_method.ClassificationMethod] = None
        # The description property
        self._description: Optional[str] = None
        # The name property
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The publisherName property
        self._publisher_name: Optional[str] = None
        # The rulePackageId property
        self._rule_package_id: Optional[str] = None
        # The rulePackageType property
        self._rule_package_type: Optional[str] = None
        # The scope property
        self._scope: Optional[sensitive_type_scope.SensitiveTypeScope] = None
        # The sensitiveTypeSource property
        self._sensitive_type_source: Optional[sensitive_type_source.SensitiveTypeSource] = None
        # The state property
        self._state: Optional[str] = None
    
    @property
    def classification_method(self,) -> Optional[classification_method.ClassificationMethod]:
        """
        Gets the classificationMethod property value. The classificationMethod property
        Returns: Optional[classification_method.ClassificationMethod]
        """
        return self._classification_method
    
    @classification_method.setter
    def classification_method(self,value: Optional[classification_method.ClassificationMethod] = None) -> None:
        """
        Sets the classificationMethod property value. The classificationMethod property
        Args:
            value: Value to set for the classification_method property.
        """
        self._classification_method = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SensitiveType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SensitiveType
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SensitiveType()
    
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
        from . import classification_method, entity, sensitive_type_scope, sensitive_type_source

        fields: Dict[str, Callable[[Any], None]] = {
            "classificationMethod": lambda n : setattr(self, 'classification_method', n.get_enum_value(classification_method.ClassificationMethod)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "publisherName": lambda n : setattr(self, 'publisher_name', n.get_str_value()),
            "rulePackageId": lambda n : setattr(self, 'rule_package_id', n.get_str_value()),
            "rulePackageType": lambda n : setattr(self, 'rule_package_type', n.get_str_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_enum_value(sensitive_type_scope.SensitiveTypeScope)),
            "sensitiveTypeSource": lambda n : setattr(self, 'sensitive_type_source', n.get_enum_value(sensitive_type_source.SensitiveTypeSource)),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
            value: Value to set for the publisher_name property.
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
            value: Value to set for the rule_package_id property.
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
            value: Value to set for the rule_package_type property.
        """
        self._rule_package_type = value
    
    @property
    def scope(self,) -> Optional[sensitive_type_scope.SensitiveTypeScope]:
        """
        Gets the scope property value. The scope property
        Returns: Optional[sensitive_type_scope.SensitiveTypeScope]
        """
        return self._scope
    
    @scope.setter
    def scope(self,value: Optional[sensitive_type_scope.SensitiveTypeScope] = None) -> None:
        """
        Sets the scope property value. The scope property
        Args:
            value: Value to set for the scope property.
        """
        self._scope = value
    
    @property
    def sensitive_type_source(self,) -> Optional[sensitive_type_source.SensitiveTypeSource]:
        """
        Gets the sensitiveTypeSource property value. The sensitiveTypeSource property
        Returns: Optional[sensitive_type_source.SensitiveTypeSource]
        """
        return self._sensitive_type_source
    
    @sensitive_type_source.setter
    def sensitive_type_source(self,value: Optional[sensitive_type_source.SensitiveTypeSource] = None) -> None:
        """
        Sets the sensitiveTypeSource property value. The sensitiveTypeSource property
        Args:
            value: Value to set for the sensitive_type_source property.
        """
        self._sensitive_type_source = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("classificationMethod", self.classification_method)
        writer.write_str_value("description", self.description)
        writer.write_str_value("name", self.name)
        writer.write_str_value("publisherName", self.publisher_name)
        writer.write_str_value("rulePackageId", self.rule_package_id)
        writer.write_str_value("rulePackageType", self.rule_package_type)
        writer.write_enum_value("scope", self.scope)
        writer.write_enum_value("sensitiveTypeSource", self.sensitive_type_source)
        writer.write_str_value("state", self.state)
    
    @property
    def state(self,) -> Optional[str]:
        """
        Gets the state property value. The state property
        Returns: Optional[str]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[str] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

