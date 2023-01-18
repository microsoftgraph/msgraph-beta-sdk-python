from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

email_identity = lazy_import('msgraph.generated.models.email_identity')
entity = lazy_import('msgraph.generated.models.entity')
payload_brand = lazy_import('msgraph.generated.models.payload_brand')
payload_complexity = lazy_import('msgraph.generated.models.payload_complexity')
payload_delivery_platform = lazy_import('msgraph.generated.models.payload_delivery_platform')
payload_detail = lazy_import('msgraph.generated.models.payload_detail')
payload_industry = lazy_import('msgraph.generated.models.payload_industry')
payload_theme = lazy_import('msgraph.generated.models.payload_theme')
simulation_attack_technique = lazy_import('msgraph.generated.models.simulation_attack_technique')
simulation_attack_type = lazy_import('msgraph.generated.models.simulation_attack_type')
simulation_content_source = lazy_import('msgraph.generated.models.simulation_content_source')
simulation_content_status = lazy_import('msgraph.generated.models.simulation_content_status')

class Payload(entity.Entity):
    @property
    def brand(self,) -> Optional[payload_brand.PayloadBrand]:
        """
        Gets the brand property value. The brand property
        Returns: Optional[payload_brand.PayloadBrand]
        """
        return self._brand
    
    @brand.setter
    def brand(self,value: Optional[payload_brand.PayloadBrand] = None) -> None:
        """
        Sets the brand property value. The brand property
        Args:
            value: Value to set for the brand property.
        """
        self._brand = value
    
    @property
    def complexity(self,) -> Optional[payload_complexity.PayloadComplexity]:
        """
        Gets the complexity property value. The complexity property
        Returns: Optional[payload_complexity.PayloadComplexity]
        """
        return self._complexity
    
    @complexity.setter
    def complexity(self,value: Optional[payload_complexity.PayloadComplexity] = None) -> None:
        """
        Sets the complexity property value. The complexity property
        Args:
            value: Value to set for the complexity property.
        """
        self._complexity = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new payload and sets the default values.
        """
        super().__init__()
        # The brand property
        self._brand: Optional[payload_brand.PayloadBrand] = None
        # The complexity property
        self._complexity: Optional[payload_complexity.PayloadComplexity] = None
        # The createdBy property
        self._created_by: Optional[email_identity.EmailIdentity] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The description property
        self._description: Optional[str] = None
        # The detail property
        self._detail: Optional[payload_detail.PayloadDetail] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The industry property
        self._industry: Optional[payload_industry.PayloadIndustry] = None
        # The isAutomated property
        self._is_automated: Optional[bool] = None
        # The isControversial property
        self._is_controversial: Optional[bool] = None
        # The isCurrentEvent property
        self._is_current_event: Optional[bool] = None
        # The language property
        self._language: Optional[str] = None
        # The lastModifiedBy property
        self._last_modified_by: Optional[email_identity.EmailIdentity] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The payloadTags property
        self._payload_tags: Optional[List[str]] = None
        # The platform property
        self._platform: Optional[payload_delivery_platform.PayloadDeliveryPlatform] = None
        # The predictedCompromiseRate property
        self._predicted_compromise_rate: Optional[float] = None
        # The simulationAttackType property
        self._simulation_attack_type: Optional[simulation_attack_type.SimulationAttackType] = None
        # The source property
        self._source: Optional[simulation_content_source.SimulationContentSource] = None
        # The status property
        self._status: Optional[simulation_content_status.SimulationContentStatus] = None
        # The technique property
        self._technique: Optional[simulation_attack_technique.SimulationAttackTechnique] = None
        # The theme property
        self._theme: Optional[payload_theme.PayloadTheme] = None
    
    @property
    def created_by(self,) -> Optional[email_identity.EmailIdentity]:
        """
        Gets the createdBy property value. The createdBy property
        Returns: Optional[email_identity.EmailIdentity]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[email_identity.EmailIdentity] = None) -> None:
        """
        Sets the createdBy property value. The createdBy property
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The createdDateTime property
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The createdDateTime property
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Payload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Payload
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Payload()
    
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
    
    @property
    def detail(self,) -> Optional[payload_detail.PayloadDetail]:
        """
        Gets the detail property value. The detail property
        Returns: Optional[payload_detail.PayloadDetail]
        """
        return self._detail
    
    @detail.setter
    def detail(self,value: Optional[payload_detail.PayloadDetail] = None) -> None:
        """
        Sets the detail property value. The detail property
        Args:
            value: Value to set for the detail property.
        """
        self._detail = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "brand": lambda n : setattr(self, 'brand', n.get_enum_value(payload_brand.PayloadBrand)),
            "complexity": lambda n : setattr(self, 'complexity', n.get_enum_value(payload_complexity.PayloadComplexity)),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(email_identity.EmailIdentity)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "detail": lambda n : setattr(self, 'detail', n.get_object_value(payload_detail.PayloadDetail)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "industry": lambda n : setattr(self, 'industry', n.get_enum_value(payload_industry.PayloadIndustry)),
            "is_automated": lambda n : setattr(self, 'is_automated', n.get_bool_value()),
            "is_controversial": lambda n : setattr(self, 'is_controversial', n.get_bool_value()),
            "is_current_event": lambda n : setattr(self, 'is_current_event', n.get_bool_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_object_value(email_identity.EmailIdentity)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "payload_tags": lambda n : setattr(self, 'payload_tags', n.get_collection_of_primitive_values(str)),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(payload_delivery_platform.PayloadDeliveryPlatform)),
            "predicted_compromise_rate": lambda n : setattr(self, 'predicted_compromise_rate', n.get_float_value()),
            "simulation_attack_type": lambda n : setattr(self, 'simulation_attack_type', n.get_enum_value(simulation_attack_type.SimulationAttackType)),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(simulation_content_source.SimulationContentSource)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(simulation_content_status.SimulationContentStatus)),
            "technique": lambda n : setattr(self, 'technique', n.get_enum_value(simulation_attack_technique.SimulationAttackTechnique)),
            "theme": lambda n : setattr(self, 'theme', n.get_enum_value(payload_theme.PayloadTheme)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def industry(self,) -> Optional[payload_industry.PayloadIndustry]:
        """
        Gets the industry property value. The industry property
        Returns: Optional[payload_industry.PayloadIndustry]
        """
        return self._industry
    
    @industry.setter
    def industry(self,value: Optional[payload_industry.PayloadIndustry] = None) -> None:
        """
        Sets the industry property value. The industry property
        Args:
            value: Value to set for the industry property.
        """
        self._industry = value
    
    @property
    def is_automated(self,) -> Optional[bool]:
        """
        Gets the isAutomated property value. The isAutomated property
        Returns: Optional[bool]
        """
        return self._is_automated
    
    @is_automated.setter
    def is_automated(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAutomated property value. The isAutomated property
        Args:
            value: Value to set for the isAutomated property.
        """
        self._is_automated = value
    
    @property
    def is_controversial(self,) -> Optional[bool]:
        """
        Gets the isControversial property value. The isControversial property
        Returns: Optional[bool]
        """
        return self._is_controversial
    
    @is_controversial.setter
    def is_controversial(self,value: Optional[bool] = None) -> None:
        """
        Sets the isControversial property value. The isControversial property
        Args:
            value: Value to set for the isControversial property.
        """
        self._is_controversial = value
    
    @property
    def is_current_event(self,) -> Optional[bool]:
        """
        Gets the isCurrentEvent property value. The isCurrentEvent property
        Returns: Optional[bool]
        """
        return self._is_current_event
    
    @is_current_event.setter
    def is_current_event(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCurrentEvent property value. The isCurrentEvent property
        Args:
            value: Value to set for the isCurrentEvent property.
        """
        self._is_current_event = value
    
    @property
    def language(self,) -> Optional[str]:
        """
        Gets the language property value. The language property
        Returns: Optional[str]
        """
        return self._language
    
    @language.setter
    def language(self,value: Optional[str] = None) -> None:
        """
        Sets the language property value. The language property
        Args:
            value: Value to set for the language property.
        """
        self._language = value
    
    @property
    def last_modified_by(self,) -> Optional[email_identity.EmailIdentity]:
        """
        Gets the lastModifiedBy property value. The lastModifiedBy property
        Returns: Optional[email_identity.EmailIdentity]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[email_identity.EmailIdentity] = None) -> None:
        """
        Sets the lastModifiedBy property value. The lastModifiedBy property
        Args:
            value: Value to set for the lastModifiedBy property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def payload_tags(self,) -> Optional[List[str]]:
        """
        Gets the payloadTags property value. The payloadTags property
        Returns: Optional[List[str]]
        """
        return self._payload_tags
    
    @payload_tags.setter
    def payload_tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the payloadTags property value. The payloadTags property
        Args:
            value: Value to set for the payloadTags property.
        """
        self._payload_tags = value
    
    @property
    def platform(self,) -> Optional[payload_delivery_platform.PayloadDeliveryPlatform]:
        """
        Gets the platform property value. The platform property
        Returns: Optional[payload_delivery_platform.PayloadDeliveryPlatform]
        """
        return self._platform
    
    @platform.setter
    def platform(self,value: Optional[payload_delivery_platform.PayloadDeliveryPlatform] = None) -> None:
        """
        Sets the platform property value. The platform property
        Args:
            value: Value to set for the platform property.
        """
        self._platform = value
    
    @property
    def predicted_compromise_rate(self,) -> Optional[float]:
        """
        Gets the predictedCompromiseRate property value. The predictedCompromiseRate property
        Returns: Optional[float]
        """
        return self._predicted_compromise_rate
    
    @predicted_compromise_rate.setter
    def predicted_compromise_rate(self,value: Optional[float] = None) -> None:
        """
        Sets the predictedCompromiseRate property value. The predictedCompromiseRate property
        Args:
            value: Value to set for the predictedCompromiseRate property.
        """
        self._predicted_compromise_rate = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("brand", self.brand)
        writer.write_enum_value("complexity", self.complexity)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_object_value("detail", self.detail)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("industry", self.industry)
        writer.write_bool_value("isAutomated", self.is_automated)
        writer.write_bool_value("isControversial", self.is_controversial)
        writer.write_bool_value("isCurrentEvent", self.is_current_event)
        writer.write_str_value("language", self.language)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("payloadTags", self.payload_tags)
        writer.write_enum_value("platform", self.platform)
        writer.write_float_value("predictedCompromiseRate", self.predicted_compromise_rate)
        writer.write_enum_value("simulationAttackType", self.simulation_attack_type)
        writer.write_enum_value("source", self.source)
        writer.write_enum_value("status", self.status)
        writer.write_enum_value("technique", self.technique)
        writer.write_enum_value("theme", self.theme)
    
    @property
    def simulation_attack_type(self,) -> Optional[simulation_attack_type.SimulationAttackType]:
        """
        Gets the simulationAttackType property value. The simulationAttackType property
        Returns: Optional[simulation_attack_type.SimulationAttackType]
        """
        return self._simulation_attack_type
    
    @simulation_attack_type.setter
    def simulation_attack_type(self,value: Optional[simulation_attack_type.SimulationAttackType] = None) -> None:
        """
        Sets the simulationAttackType property value. The simulationAttackType property
        Args:
            value: Value to set for the simulationAttackType property.
        """
        self._simulation_attack_type = value
    
    @property
    def source(self,) -> Optional[simulation_content_source.SimulationContentSource]:
        """
        Gets the source property value. The source property
        Returns: Optional[simulation_content_source.SimulationContentSource]
        """
        return self._source
    
    @source.setter
    def source(self,value: Optional[simulation_content_source.SimulationContentSource] = None) -> None:
        """
        Sets the source property value. The source property
        Args:
            value: Value to set for the source property.
        """
        self._source = value
    
    @property
    def status(self,) -> Optional[simulation_content_status.SimulationContentStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[simulation_content_status.SimulationContentStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[simulation_content_status.SimulationContentStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def technique(self,) -> Optional[simulation_attack_technique.SimulationAttackTechnique]:
        """
        Gets the technique property value. The technique property
        Returns: Optional[simulation_attack_technique.SimulationAttackTechnique]
        """
        return self._technique
    
    @technique.setter
    def technique(self,value: Optional[simulation_attack_technique.SimulationAttackTechnique] = None) -> None:
        """
        Sets the technique property value. The technique property
        Args:
            value: Value to set for the technique property.
        """
        self._technique = value
    
    @property
    def theme(self,) -> Optional[payload_theme.PayloadTheme]:
        """
        Gets the theme property value. The theme property
        Returns: Optional[payload_theme.PayloadTheme]
        """
        return self._theme
    
    @theme.setter
    def theme(self,value: Optional[payload_theme.PayloadTheme] = None) -> None:
        """
        Sets the theme property value. The theme property
        Args:
            value: Value to set for the theme property.
        """
        self._theme = value
    

