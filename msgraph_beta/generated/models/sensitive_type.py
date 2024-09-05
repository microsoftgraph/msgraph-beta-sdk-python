from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .classification_method import ClassificationMethod
    from .entity import Entity
    from .sensitive_type_scope import SensitiveTypeScope
    from .sensitive_type_source import SensitiveTypeSource

from .entity import Entity

@dataclass
class SensitiveType(Entity):
    # The classificationMethod property
    classification_method: Optional[ClassificationMethod] = None
    # The description property
    description: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The publisherName property
    publisher_name: Optional[str] = None
    # The rulePackageId property
    rule_package_id: Optional[str] = None
    # The rulePackageType property
    rule_package_type: Optional[str] = None
    # The scope property
    scope: Optional[SensitiveTypeScope] = None
    # The sensitiveTypeSource property
    sensitive_type_source: Optional[SensitiveTypeSource] = None
    # The state property
    state: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SensitiveType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SensitiveType
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SensitiveType()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .classification_method import ClassificationMethod
        from .entity import Entity
        from .sensitive_type_scope import SensitiveTypeScope
        from .sensitive_type_source import SensitiveTypeSource

        from .classification_method import ClassificationMethod
        from .entity import Entity
        from .sensitive_type_scope import SensitiveTypeScope
        from .sensitive_type_source import SensitiveTypeSource

        fields: Dict[str, Callable[[Any], None]] = {
            "classificationMethod": lambda n : setattr(self, 'classification_method', n.get_enum_value(ClassificationMethod)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "publisherName": lambda n : setattr(self, 'publisher_name', n.get_str_value()),
            "rulePackageId": lambda n : setattr(self, 'rule_package_id', n.get_str_value()),
            "rulePackageType": lambda n : setattr(self, 'rule_package_type', n.get_str_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_collection_of_enum_values(SensitiveTypeScope)),
            "sensitiveTypeSource": lambda n : setattr(self, 'sensitive_type_source', n.get_enum_value(SensitiveTypeSource)),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
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
    

